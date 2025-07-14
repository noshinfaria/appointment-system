from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Division(Base):
    __tablename__ = "divisions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    districts = relationship("District", back_populates="division")

class District(Base):
    __tablename__ = "districts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    division_id = Column(Integer, ForeignKey("divisions.id"))
    division = relationship("Division", back_populates="districts")
    thanas = relationship("Thana", back_populates="district")

class Thana(Base):
    __tablename__ = "thanas"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    district_id = Column(Integer, ForeignKey("districts.id"))
    district = relationship("District", back_populates="thanas")
