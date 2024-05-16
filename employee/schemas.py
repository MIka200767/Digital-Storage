from typing import List, Optional
from pydantic import BaseModel , Field, EmailStr
from datetime import datetime
from devices.schemas import SchemaCreateDevice



class EmployeeSchema(BaseModel):
    id: int
    name: str = Field(min_length=3)
    email: EmailStr
    phone: str = Field(min_length=6)
    updated_at: Optional[str]=None
    created_at: datetime
    devices: Optional[List[SchemaCreateDevice]]=None
    team_id: Optional[int]=None


    class Config:
        from_attributes = True


class ResponseModel(BaseModel):
    name: str = Field(min_length=3)
    email: EmailStr
    phone: str = Field(min_length=6)
    updated_at: Optional[str]=None
    created_at: datetime
    team_id: Optional[int]=None
    devices: list

# for creating employee
class CreatedEmployeeSchema(BaseModel):
    name: str = Field(min_length=3)
    email: EmailStr
    phone: str = Field(min_length=6)
    created_at: datetime
    team_id: Optional[int]=None


class ResponseSchemaCreating(BaseModel):
    code: int
    status: str
    message: str
    response: CreatedEmployeeSchema


# for getting employees or employee
class ResponseEmployee(BaseModel):
    code: int
    status: str
    message: str
    response: List[EmployeeSchema]

# schema for getting employee by email

class SchemasEmployee(BaseModel):
    code: int
    status: str
    message: str
    response: EmployeeSchema

#for updating employee
class SchemaUpdateEmployee(BaseModel):
    code: int
    status: str
    message: str
    response: EmployeeSchema


#for deleting employee
class SchemaDelete(BaseModel):
    code: int



