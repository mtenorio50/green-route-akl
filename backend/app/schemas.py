from pydantic import BaseModel
from typing import Optional, List

class Stop(BaseModel):
    stop_id: str
    name: str
    lat: float
    lon: float

class VehiclePosition(BaseModel):
    vehicle_id: str
    trip_id: Optional[str] = None
    route_id: Optional[str] = None
    lat: float
    lon: float
    bearing: Optional[float] = None
    speed_kmh: Optional[float] = None
    updated_at: Optional[str] = None
