from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from oath2 import get_current_user, active_user_role
from . import crud
from devices.schemas import DevicesSchemas, ReponseCreating, ResposneGet, ResponseUpdate, ResponseDelete
from database import get_db
from employee.crud import get_employee_by_id

router = APIRouter(dependencies=[Depends(get_current_user)])

@router.post("/create", response_model=ReponseCreating, dependencies=[Depends(active_user_role)])
async def create_device(request: DevicesSchemas, db: Session=Depends(get_db)):
    existing_device = crud.get_device_by_serial_num(db, serial_num=request.serial_number)
    if existing_device:
        raise HTTPException(status_code=400, detail="Device Already Exists")
    employee = get_employee_by_id(db, employee_id=request.employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail=f"No Employee by ID {request.employee_id}")
    _device = crud.create_device(db, device=request)
    response_data = {"code": 200, "status": "OK", "message": "Successfully created the device", "response": _device}
    return response_data


@router.get("/all", response_model=ResposneGet)
async def read_all(db: Session=Depends(get_db)):
    _device = crud.get_all_device(db)
    response_data = {"code": 200, "status": "OK", "message": "Fetched all devices", "response": _device}
    return response_data


@router.get("/{id}", response_model=ResposneGet)
async def read_device(id: int, db: Session=Depends(get_db)):
    _device = crud.get_device_by_id(db, device_id=id)
    if not _device:
        raise HTTPException(status_code=404, detail="Device Not Found")
    response_data = {"code": 200, "status": "OK", "message": "Fetched the device", "response": _device}
    return response_data


@router.post("/update", response_model=ResponseUpdate, dependencies=[Depends(active_user_role)])
async def update_device(device: DevicesSchemas, db: Session=Depends(get_db)):
    existing_device = crud.get_device_by_serial_num(db, serial_num=device.serial_number)
    if not existing_device:
        raise HTTPException(status_code=404, detail="Device Not Found")
    _device = crud.update_device(db, serial_number=device.serial_number, created_at=device.created_at, updated_at=device.updated_at, 
                      component1=device.component1, component2=device.component2, component3=device.component3, component4=device.component4, component5=device.component5, 
                      component6=device.component6, component7=device.component7, component8=device.component8, employee_id=device.employee_id)
    response_data = {"code": 200, "status": "OK", "message": "Updated successfully", "response": _device}
    return response_data


@router.delete("/{id}/delete", response_model=ResponseDelete, dependencies=[Depends(active_user_role)])
async def delete_device(id: int, db: Session=Depends(get_db)):  
    existing_device = crud.get_device_by_id(db, device_id=id)
    if not existing_device:
        raise HTTPException(status_code=404, detail="Device Not Found")
    _device = crud.delete_device(db, device_id=id)
    deleted_image = crud.delete_image(db=db, serial_num=existing_device.serial_number)
    response_data = {"code": 204}
    return response_data