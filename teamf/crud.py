from sqlalchemy.orm import Session
from models import Teams
from teamf.schemas import TeamSchema


def create_team(db:Session, team: TeamSchema):
    _team = Teams(name=team.name)
    db.add(_team)
    db.commit()
    db.refresh(_team)
    return _team

def get_team(db:Session):
    return db.query(Teams).all()

def get_team_by_name(db:Session, team_name: str):
    return db.query(Teams).filter(Teams.name == team_name).first()

def get_team_by_id(db:Session, team_id: int):
    return db.query(Teams).filter(Teams.id == team_id).first()

def update_team(db:Session, team_id: int, name: str):
    _team = get_team_by_id(db, team_id=team_id)
    _team.name = name
    db.commit()
    db.refresh(_team)
    return _team

def remove_team(db:Session, team_name:str):
    _team = get_team_by_name(db=db, team_name=team_name)
    db.delete(_team)
    db.commit()

