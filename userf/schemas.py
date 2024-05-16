from typing import Optional, TypeVar, List
from pydantic import BaseModel , Field, EmailStr


T = TypeVar('T')

class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=6)
    is_admin: bool

    class Config:
        from_attributes = True


class ResponseSchema(BaseModel):
    status: str
    message: str
    response: Optional[T]=None


class ReturnScheme(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=6)
    is_admin: bool


class Schema_response_list(BaseModel):
    status: str
    message: str
    response: List[ReturnScheme]


class Schema_response(BaseModel):
    code: int 
    status: str
    message: str
    response: ReturnScheme


class Schema_delete(BaseModel):
    code: int




