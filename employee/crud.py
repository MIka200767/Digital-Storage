from sqlalchemy.orm import Session
from models import Employees
from employee.schemas import EmployeeSchema
from datetime import datetime
from pydantic import EmailStr


def create_employee(db: Session, employee: EmployeeSchema):
    new_employee = Employees(name=employee.name, email=employee.email, phone=employee.phone, updated_at=employee.updated_at, created_at=employee.created_at, team_id=employee.team_id)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def get_all_employees(db:Session):
    return db.query(Employees).all()

def get_employee_by_id(db:Session, employee_id: int):
    return db.query(Employees).filter(Employees.id == employee_id).first()

def get_employee_by_email(db:Session, employee_email: str):
    return db.query(Employees).filter(Employees.email==employee_email).first()

def update_employee(db:Session, name: str, email: EmailStr, phone: str, updated_at: str, created_at: datetime, team_id: int):
    _employee = get_employee_email(db, employee_email=email)
    _employee.name = name
    _employee.email = email
    _employee.phone = phone
    _employee.updated_at = updated_at
    _employee.created_at = created_at
    _employee.team_id = team_id
    db.commit()
    db.refresh(_employee)
    return _employee

def delete_employee(db:Session, employee_id):
    _employee = get_employee_by_id(db, employee_id=employee_id)
    db.delete(_employee)
    db.commit()

def get_employee_email(db, employee_email: str):
    return db.query(Employees).filter(Employees.email==employee_email).first()
