from sqlalchemy.orm import Session
from models import Users
from userf.schemas import UserSchema
from pydantic import EmailStr
from hash import Hash


def create_user(db:Session, user: UserSchema):
    _user = Users(name=user.name, email=user.email, password=Hash.bcrypt(user.password), is_admin=user.is_admin)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


def get_all_users(db:Session):
    return db.query(Users).all()


def get_user_by_id(db:Session, user_id:int):
    return db.query(Users).filter(Users.id==user_id).first()


def update_user(db:Session, user_id:int, name:str, email: EmailStr, password: str, is_admin:bool):
    _user=get_user_by_id(db=db, user_id=user_id)
    _user.name=name
    _user.email=email
    _user.password=password
    _user.is_admin=is_admin
    db.commit()
    db.refresh(_user)
    return _user


def delete_user(db:Session, user_id):
    _user = get_user_by_id(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()
    
# Validations
def get_email(db:Session, user_email):
    return db.query(Users).filter(Users.email==user_email).first()
 