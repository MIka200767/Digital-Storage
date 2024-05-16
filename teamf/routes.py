from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud
from teamf.schemas import RequestTeamName, Response, Schmea_delete, ResponseUpdate, Schema_response
from database import get_db
from oath2 import get_current_user, active_user_role

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.post("/create", dependencies=[Depends(active_user_role)])
async def create(request: RequestTeamName, db: Session=Depends(get_db)):
    existing_team = crud.get_team_by_name(db, team_name=request.name)
    if existing_team:
        raise HTTPException(status_code=400, detail="Team Already Exists")
    created_team = crud.create_team(db, team=request)
    return Response(code=200, status="OK", message="Team created successfully", result=created_team.name).model_dump(exclude_none=True)


@router.get("/", response_model=Schema_response)
async def read_all(db: Session = Depends(get_db)):
    _team = crud.get_team(db)
    if not _team:
        raise HTTPException(status_code=404, detail="Team Does Not Exist")
    response_data =  {"code": 200, "status": "OK", "message": "Success fetch all data", "response":_team}
    return response_data


@router.get("/{name}")
async def read_by_name(name: str, db: Session=Depends(get_db)):
    _team = crud.get_team_by_name(db, name)
    if not _team:
        raise HTTPException(status_code=404, detail=f"No Team by the name {name}")
    return Response(code=200, status="OK", message="Success get data", result=_team).model_dump(exclude_none=True)


@router.post("/update", response_model=ResponseUpdate, dependencies=[Depends(active_user_role)])
async def update_team(request: RequestTeamName, db: Session=Depends(get_db)):
    existing_team = crud.get_team_by_id(db, team_id=request.id)
    if not existing_team:
        raise HTTPException(status_code=404, detail=f"No Team By the id {request.id}")
    _team = crud.update_team(db, team_id=request.id, name=request.name)
    response_data = {"code": 200, "status": "OK", "message": "Updated Successfully", "response": _team}
    return response_data


@router.delete("/{team_name}/delete", response_model=Schmea_delete, dependencies=[Depends(active_user_role)])
async def delete(team_name: str, db: Session=Depends(get_db)):
    existing_team = crud.get_team_by_name(db, team_name=team_name)
    if not existing_team:
        raise HTTPException(status_code=404, detail=f"No Team found with name {team_name}")
    crud.remove_team(db,team_name=team_name)
    response_data = {"code": 204}
    return response_data
