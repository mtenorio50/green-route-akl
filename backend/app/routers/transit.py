from fastapi import APIRouter, HTTPException
from typing import List
from ..at_client import ATClient
from ..schemas import Stop, VehiclePosition

router = APIRouter(prefix="/api/v1", tags=["transit"])
client = ATClient()


@router.get("/stops", response_model=List[Stop])
async def list_stops():
    try:
        raw = await client.get_gtfs_stops(page_size=500)
        # Map raw JSON:API to our simplified schema
        # Adjust parsing to actual AT response shape
        items = []
        for item in raw.get("data", []):
            attrs = item.get("attributes", {})
            items.append(Stop(
                stop_id=str(attrs.get("stop_id") or item.get("id")),
                name=attrs.get("stop_name") or attrs.get("name") or "Stop",
                lat=float(attrs.get("stop_lat") or attrs.get("lat")),
                lon=float(attrs.get("stop_lon") or attrs.get("lon")),
            ))
        return items
    except Exception as e:
        raise HTTPException(
            status_code=502, detail=f"AT stops fetch failed: {e}")


@router.get("/routes")
async def get_routes():
    """Get all available bus/train routes in Auckland"""
    try:
        # Use the routes data that's actually available
        raw = await client.get_routes()
        items = []
        for route in raw.get("data", []):
            attrs = route.get("attributes", {})
            route_type_names = {
                0: "Tram", 1: "Subway", 2: "Rail", 3: "Bus",
                4: "Ferry", 5: "Cable tram", 6: "Aerial lift", 7: "Funicular"
            }
            items.append({
                "route_id": attrs.get("route_id"),
                "route_name": attrs.get("route_short_name") or attrs.get("route_long_name", "Unknown"),
                "route_type": attrs.get("route_type"),
                "route_type_name": route_type_names.get(attrs.get("route_type"), "Unknown"),
                "agency_id": attrs.get("agency_id")
            })
        return items
    except Exception as e:
        raise HTTPException(
            status_code=502, detail=f"AT routes fetch failed: {e}")


@router.get("/vehicle-positions", response_model=List[VehiclePosition])
async def vehicle_positions(route_id: str | None = None):
    """
    Returns real-time vehicle position data from Auckland Transport GTFS-RT feeds.
    """
    try:
        raw = await client.get_vehicle_positions(route_id=route_id)

        items = []

        # Ensure raw is a dictionary
        if not isinstance(raw, dict):
            print(f"Expected dict, got {type(raw)}: {raw}")
            return []

        # Handle real Auckland Transport GTFS-RT response format
        if "response" in raw and raw.get("status") != "ERROR":
            for entity in raw.get("response", []):
                if not isinstance(entity, dict):
                    continue

                vehicle_data = entity.get("vehicle", {})
                position = vehicle_data.get("position", {})
                trip = vehicle_data.get("trip", {})
                vehicle_info = vehicle_data.get("vehicle", {})

                # Extract position data
                lat = position.get("latitude")
                lon = position.get("longitude")

                if lat is not None and lon is not None:
                    # Convert speed from m/s to km/h if present
                    speed_ms = position.get("speed")
                    speed_kmh = round(
                        speed_ms * 3.6, 1) if speed_ms is not None else None

                    # Convert timestamp to ISO string if it's a number
                    timestamp = vehicle_data.get("timestamp")
                    if isinstance(timestamp, (int, float)):
                        from datetime import datetime
                        updated_at = datetime.fromtimestamp(
                            timestamp).isoformat() + "Z"
                    else:
                        updated_at = str(timestamp) if timestamp else None

                    items.append(VehiclePosition(
                        vehicle_id=vehicle_info.get("id") or vehicle_info.get(
                            "label") or entity.get("id", "unknown"),
                        trip_id=trip.get("trip_id"),
                        route_id=trip.get("route_id"),
                        lat=float(lat),
                        lon=float(lon),
                        bearing=position.get("bearing"),
                        speed_kmh=speed_kmh,
                        updated_at=updated_at,
                    ))

        return items
    except Exception as e:
        raise HTTPException(
            status_code=502, detail=f"Vehicle positions fetch failed: {e}")
