from pydantic import BaseModel
from typing import List, Optional

class ModbusRegister(BaseModel):
    address: int
    name: str
    type: str
    value: float
    unit: str

class Device(BaseModel):
    id: str
    name: str
    ip: str
    port: int
    slave_id: int
    online: bool
    registers: List[ModbusRegister] = []

class Alarm(BaseModel):
    id: str
    device_id: str
    register: str
    message: str
    level: str
    timestamp: float
    acknowledged: bool = False
    acknowledged_by: Optional[str] = None
    acknowledged_at: Optional[float] = None
