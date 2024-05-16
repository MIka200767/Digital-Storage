from typing import Optional, Text, List, Union
from pydantic import BaseModel , Field
from datetime import datetime


class DevicesSchemas(BaseModel):
    serial_number: Text
    created_at: datetime
    updated_at: Optional[str]=None
    component1: Optional[str]=None
    component2: Optional[str]=None
    component3: Optional[str]=None
    component4: Optional[str]=None
    component5: Optional[str]=None
    component6: Optional[str]=None
    component7: Optional[str]=None
    component8: Optional[str]=None
    employee_id: int

    class Config:
        from_attributes = True

#schema for creating device
class SchemaCreateDevice(BaseModel):
    qr: str
    serial_number: Text
    created_at: datetime
    component1: Optional[str]=None
    component2: Optional[str]=None
    component3: Optional[str]=None
    component4: Optional[str]=None
    component5: Optional[str]=None
    component6: Optional[str]=None
    component7: Optional[str]=None
    component8: Optional[str]=None
    employee_id: int
    

class ReponseCreating(BaseModel):
    code: int
    status: str
    message: str    
    response: SchemaCreateDevice

# return devices or device
class SchemaGetDevice(BaseModel):
    qr: str
    serial_number: Text
    created_at: datetime
    component1: Optional[str]=None
    component2: Optional[str]=None
    component3: Optional[str]=None
    component4: Optional[str]=None
    component5: Optional[str]=None
    component6: Optional[str]=None
    component7: Optional[str]=None
    component8: Optional[str]=None
    employee_id: Optional[int]=None

class ResposneGet(BaseModel):
    code: int
    status: str
    message: str
    response: Union[SchemaGetDevice, List[SchemaGetDevice]]

# return updated device

class ResponseUpdate(BaseModel):
    code: int
    status: str
    message: str
    response: DevicesSchemas

class ResponseDelete(BaseModel):
    code: int