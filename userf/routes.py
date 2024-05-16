from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud
from userf.schemas import UserSchema, Schema_response_list, Schema_response, Schema_delete
from database import get_db
from oath2 import get_current_user, active_user_role


router = APIRouter(dependencies=[Depends(get_current_user)])

@router.post("/create", dependencies=[Depends(active_user_role)])
async def create(request: UserSchema, db: Session=Depends(get_db)):
    existing_employee = crud.get_email(db, user_email=request.email)
    if existing_employee:
        raise HTTPException(status_code=400, detail="User with this email already exists")
    created_user = crud.create_user(db, user=request)
    response_data = {"code": 200, "status": "OK", "message": "User Created :)", "response": created_user}
    return response_data


@router.get("/all", response_model= Schema_response_list)
async def read_all(db: Session=Depends(get_db)):
    read_all_users = crud.get_all_users(db)
    response_data =  {"code": 200, "status": "OK", "message": "Success fetch all data", "response":read_all_users}
    return response_data
    

@router.get("/{id}", response_model=Schema_response)
async def read_by_id(id: int, db: Session = Depends(get_db)):
    _user = crud.get_user_by_id(db, id)
    if not _user:
        raise HTTPException(status_code=404, detail="User Not Found")
    response_data = {"code": 200, "status": "OK", "message": "User Returned :)", "response": _user}
    return response_data


@router.post("/update", response_model=Schema_response, dependencies=[Depends(active_user_role)])
async def update_user(request: UserSchema, db: Session=Depends(get_db)):
    user = crud.get_email(db, user_email=request.email)
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    _user = crud.update_user(db, user_id=request.id, name=request.name, email=request.email, password=request.password, is_admin=request.is_admin)
    response_data = {"code": 200, "status": "OK", "message": "Updated Successfully", "response": _user}
    return response_data


@router.delete("{id}/delete", response_model=Schema_delete, dependencies=[Depends(active_user_role)])
async def delete_user(id: int, db: Session=Depends(get_db)):
    user = crud.get_user_by_id(db, user_id=id)
    if not user:
        raise HTTPException(status_code=404, detail=f"there is no user by id {id}")
    deleted_user = crud.delete_user(db, id)
    response_data = {"code": 204}
    return response_data

