from pydantic import BaseModel

class DivisionBase(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class DistrictBase(BaseModel):
    id: int
    name: str
    division_id: int
    class Config:
        orm_mode = True

class ThanaBase(BaseModel):
    id: int
    name: str
    district_id: int
    class Config:
        orm_mode = True
