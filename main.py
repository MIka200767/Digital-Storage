from fastapi import FastAPI
import models
from database import engine
from teamf.routes import router as team_routes
from userf.routes import router as user_routes
from employee.routes import router as employee_routes
from devices.routes import router as device_router
from authentication import router as login_router
from qr_folder.routes import router as qr_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(team_routes, prefix="/team", tags=["teams"])
app.include_router(employee_routes, prefix="/employee", tags=["employees"])
app.include_router(user_routes, prefix="/user", tags=["users"])
app.include_router(device_router, prefix="/device", tags=["devices"])
app.include_router(login_router, prefix="/auth", tags=["Authentication"])
app.include_router(qr_router, prefix="/qr", tags=["qr_code"])


