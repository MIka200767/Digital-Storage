from sqlalchemy.orm import Session
from models import Devices
from devices.schemas import DevicesSchemas
from typing import Text
from datetime import datetime
from qr_folder.qr import generate_qr_link
import os


def create_device(db:Session, device: DevicesSchemas):
    qr_link = generate_qr_link(device_serial_number=device.serial_number)
    _device = Devices( qr=qr_link, serial_number=device.serial_number, created_at=device.created_at, updated_at=device.updated_at, 
                      component1=device.component1, component2=device.component2, component3=device.component3, component4=device.component4, component5=device.component5, 
                      component6=device.component6, component7=device.component7, component8=device.component8, employee_id=device.employee_id)
    db.add(_device)
    db.commit()
    db.refresh(_device)
    return _device

def get_all_device(db:Session):
    return db.query(Devices).all()

def get_device_by_id(db:Session, device_id:int):
    return db.query(Devices).filter(Devices.id == device_id).first()

def get_device_by_serial_num(db:Session, serial_num: int):
    return db.query(Devices).filter(Devices.serial_number==serial_num).first()

def update_device(db:Session, serial_number:Text, created_at: datetime, updated_at: str, component1: str, 
                  component2: str, component3: str, component4: str, component5: str, component6: str, component7: str, component8: str, employee_id: int):
    _device = get_device_by_serial_num(db, serial_num=serial_number)
    _device.serial_number = serial_number
    _device.created_at = created_at
    _device.updated_at = updated_at
    _device.component1 = component1
    _device.component2 = component2
    _device.component3 = component3
    _device.component4 = component4
    _device.component5 = component5
    _device.component6 = component6
    _device.component7 = component7
    _device.component8 = component8
    _device.employee_id = employee_id
    db.commit()
    db.refresh(_device)
    return _device

def delete_device(db:Session, device_id: int):
    deleted_device = get_device_by_id(db=db, device_id=device_id)
    db.delete(deleted_device)
    db.commit()

def delete_image(db:Session, serial_num: Text):
    image_folder = "qr_images"
    file_path = os.path.join(image_folder, f"qr_code_{serial_num}.png")

    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Error deleting image: {file_path}")

