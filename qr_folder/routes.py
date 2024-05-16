from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import get_db
from models import Devices
from typing import Text
from devices import schemas


router = APIRouter()

@router.get("/scan_device/", response_model=schemas.ResposneGet)
async def scan_device(serial_num: Text = Query(..., title="QR Code"), db: Session = Depends(get_db)):
    device = db.query(Devices).filter(Devices.serial_number == serial_num).first()
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    response_data = {"code": 200, "status": "OK", "message": "Fetched the device", "response": device}
    return response_data

