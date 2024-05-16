from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session
from oath2 import get_current_user, active_user_role
from . import crud
from database import get_db
from employee.schemas import ResponseSchemaCreating, ResponseEmployee, SchemaUpdateEmployee, SchemaDelete, ResponseModel, SchemasEmployee
from teamf.crud import get_team_by_id


router = APIRouter(dependencies=[Depends(get_current_user)])

@router.post("/create", response_model=ResponseSchemaCreating, dependencies=[Depends(active_user_role)])
async def create_new_employee(request: ResponseModel, db: Session=Depends(get_db)):
    existing_employee = crud.get_employee_email(db, employee_email=request.email)
    if existing_employee:
        raise HTTPException(status_code=400, detail="Employee Already Exists")
    existing_team = get_team_by_id(db, team_id=request.team_id)
    if not existing_team:
        raise HTTPException(status_code=404, detail=f"No Team by iD {request.team_id}")
    created_employee = crud.create_employee(db, employee=request)
    response_data = {"code": 200, "status": "OK", "message": "Employee Created :)", "response": created_employee}
    return response_data


@router.get("/all", response_model=ResponseEmployee)
async def read(db: Session=Depends(get_db)):
    _employee = crud.get_all_employees(db)
    response_data = {"code": 200, "status": "OK", "message": "Fetched All Fata", "response": _employee}
    return response_data


@router.get("/{email}", response_model=SchemasEmployee)
async def read_by_id(email: EmailStr, db: Session=Depends(get_db)):
    _employee = crud.get_employee_by_email(db, employee_email=email)
    if not _employee:
        raise HTTPException(status_code=404, detail="Employee Not Found")
    response_data = {"code": 200, "status": "OK", "message": "Got employee by ID :)", "response": _employee}
    return response_data
    

@router.put("/update", response_model=SchemaUpdateEmployee, dependencies=[Depends(active_user_role)])
async def update_employee(request: ResponseModel, db: Session=Depends(get_db)):
    existing_employee = crud.get_employee_by_email(db, employee_email=request.email)
    if not existing_employee:
        raise HTTPException(status_code=404, detail="Employee Not Found")
    _employee = crud.update_employee(db, name=request.name, email=request.email, phone=request.phone, updated_at=request.updated_at, created_at=request.created_at, team_id=request.team_id)
    response_data = {"code": 200, "status": "OK", "message": "Employee updated :)", "response": _employee}
    return response_data


@router.delete("/delete", response_model=SchemaDelete, dependencies=[Depends(active_user_role)])
async def delete_employee(id: int, db: Session=Depends(get_db)):
    existing_employee = crud.get_employee_by_id(db, employee_id=id)
    if not existing_employee:
        raise HTTPException(status_code=404, detail=f"No Employee Found With ID {id}")
    deleted_employee = crud.delete_employee(db, id)
    response_data = {"code": 204}
    return response_data
    