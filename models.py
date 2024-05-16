from datetime import datetime, timezone
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from database import Base


class Employees(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=False, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(50), unique=True, nullable=False)
    updated_at = Column(String(50), unique=False, nullable=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc).replace(tzinfo=None))
    devices = relationship("Devices", back_populates="employees")
    teams = relationship("Teams", back_populates="employers")
    team_id = Column(Integer, ForeignKey("teams.id"))



class Devices(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True, index=True)
    qr = Column(String, unique=True, nullable=False)
    serial_number = Column(Text, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc).replace(tzinfo=None))
    updated_at = Column(String(50), unique=False, nullable=True)
    component1 = Column(String(50), unique=False, nullable=True)
    component2 = Column(String(50), unique=False, nullable=True)
    component3 = Column(String(50), unique=False, nullable=True)
    component4 = Column(String(50), unique=False, nullable=True)
    component5 = Column(String(50), unique=False, nullable=True)
    component6 = Column(String(50), unique=False, nullable=True)
    component7 = Column(String(50), unique=False, nullable=True)
    component8 = Column(String(100), unique=False, nullable=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    employees = relationship("Employees", back_populates="devices")


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=False, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(200), unique=False, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)


class Teams(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False, nullable=False)
    employers =  relationship("Employees", back_populates="teams")
