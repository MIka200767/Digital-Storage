from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from token_1 import verify_token
from jose import jwt
from token_1 import SECRET_KEY, ALGORITHM
from models import Users
from sqlalchemy.orm import Session
from database import get_db


oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_schema)): 
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Cold not validate",
        headers={"WWW-Authenticate": "Bareer"},
    )

    return verify_token(token, credentials_exception)


def get_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    decoded = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    user_email = decoded.get('sub')
    user = db.query(Users).filter(Users.email==user_email).first()
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no User with the email {user_email}")


def active_user_role(user: Users = Depends(get_user)) -> bool:
    if user.is_admin == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Permission denied")
    return True