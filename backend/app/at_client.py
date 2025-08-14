import asyncio
import time
from typing import Any, Dict, Optional
import httpx
from .config import settings

# very small in-memory cache
# key -> {"expires": float, "data": Any}
_cache: Dict[str, Dict[str, Any]] = {}


def _cache_get(key: str) -> Optional[Any]:
    item = _cache.get(key)
    if not item:
        return None
    if item["expires"] < time.time():
        _cache.pop(key, None)
        return None
    return item["data"]


def _cache_set(key: str, data: Any, ttl: int):
    # Use shorter TTL for real-time data (30 seconds)
    if "vehicle_positions" in key:
        ttl = min(ttl, 30)
    _cache[key] = {"expires": time.time() + ttl, "data": data}


class ATClient:
    def __init__(self):
        self.base = settings.at_base_url.rstrip("/")
        self.headers = {
            "Ocp-Apim-Subscription-Key": settings.at_subscription_key}
        self.client = httpx.AsyncClient(timeout=15.0, headers=self.headers)

    async def _get(self, path: str, params: Optional[dict] = None, cache_key: Optional[str] = None):
        if cache_key:
            cached = _cache_get(cache_key)
            if cached is not None:
                return cached

        # simple retry loop
        last_exc = None
        for _ in range(3):
            try:
                resp = await self.client.get(f"{self.base}{path}", params=params)
                resp.raise_for_status()
                data = resp.json()
                if cache_key:
                    _cache_set(cache_key, data, settings.cache_ttl_seconds)
                return data
            except httpx.HTTPError as exc:
                last_exc = exc
                await asyncio.sleep(0.4)
        raise last_exc

    # ---- Replace the paths with the exact AT endpoints you enable in the portal ----
    async def get_gtfs_stops(self, page_size: int = 200):
        # AT GTFS stops endpoint doesn't support pagination - returns all stops
        return await self._get(
            path="/gtfs/v3/stops",  # No parameters needed
            params=None,  # Remove page[size] parameter
            cache_key="all_stops"  # Cache all stops
        )

    async def get_routes(self):
        # Get all available routes
        return await self._get(
            path="/gtfs/v3/routes",
            params=None,
            cache_key="all_routes"
        )

    async def get_vehicle_positions(self, route_id: Optional[str] = None):
        # Get real-time vehicle positions from Auckland Transport GTFS-RT legacy endpoint
        try:
            data = await self._get(
                path="/realtime/legacy/vehiclelocations",
                params=None,
                cache_key=f"vehicle_positions_{route_id or 'all'}"
            )

            # Ensure data is a dictionary
            if not isinstance(data, dict):
                print(f"Unexpected response type: {type(data)}")
                return {
                    "status": "ERROR",
                    "response": [],
                    "error": f"Invalid response format: {type(data)}"
                }

            # Handle the GTFS-RT response structure
            # The response should have 'header' and 'entity' keys
            entities = []
            if 'entity' in data:
                entities = data['entity']
            elif 'response' in data and isinstance(data['response'], dict) and 'entity' in data['response']:
                entities = data['response']['entity']
            elif 'response' in data and isinstance(data['response'], list):
                entities = data['response']

            # Filter by route_id if specified
            if route_id:
                filtered_entities = [
                    entity for entity in entities
                    if entity.get("vehicle", {}).get("trip", {}).get("route_id") == route_id
                ]
                entities = filtered_entities

            # Return in the expected format
            return {
                "status": "OK",
                "response": entities,
                "error": None
            }

        except Exception as e:
            print(f"Failed to get real vehicle positions: {e}")
            # Return empty result with error info
            return {
                "status": "ERROR",
                "response": [],
                "error": f"Real-time data unavailable: {str(e)}"
            }
