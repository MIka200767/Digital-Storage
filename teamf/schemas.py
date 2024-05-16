from typing import Optional, Generic, TypeVar, List
from pydantic import BaseModel , Field

T = TypeVar('T')

class TeamSchema(BaseModel):
    name: str = Field(min_length=2)
    employee_id: int

    class Config:
        from_attributes = True

class RequestTeamName(BaseModel):
    id: int
    name: str

class Response(BaseModel, Generic[T]):
    code: int
    status: str
    message: str
    result: Optional[T]=None


class Schmea_delete(BaseModel):
    code: int

# get all
class TeamName(BaseModel):
    id: int
    name: str


class Schema_response(BaseModel):
    code: int 
    status: str
    message: str
    response: List[TeamName]


class ResponseUpdate(BaseModel):
    code: int
    status: str
    message: str
    response: RequestTeamName

