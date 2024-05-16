from pydantic import BaseModel , Field, EmailStr

class Login(BaseModel):
    username: EmailStr
    password: str = Field(min_length=6)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: EmailStr

