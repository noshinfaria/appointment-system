from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.address import Division, District, Thana
from app.schemas.address import DivisionBase, DistrictBase, ThanaBase

router = APIRouter()

@router.get("/divisions", response_model=list[DivisionBase])
def get_divisions(db: Session = Depends(get_db)):
    return db.query(Division).all()

@router.get("/districts/{division_id}", response_model=list[DistrictBase])
def get_districts(division_id: int, db: Session = Depends(get_db)):
    return db.query(District).filter(District.division_id == division_id).all()

@router.get("/thanas/{district_id}", response_model=list[ThanaBase])
def get_thanas(district_id: int, db: Session = Depends(get_db)):
    return db.query(Thana).filter(Thana.district_id == district_id).all()
