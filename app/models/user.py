from sqlalchemy import Column, String, Boolean, Enum, Integer, Float, ARRAY
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.database import Base
import enum

class UserType(str, enum.Enum):
    admin = "admin"
    doctor = "doctor"
    patient = "patient"

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    mobile = Column(String(14), unique=True, nullable=False)
    password = Column(String, nullable=False)
    user_type = Column(Enum(UserType), nullable=False)
    division = Column(String)
    district = Column(String)
    thana = Column(String)
    profile_image = Column(String, nullable=True)
    license_number = Column(String, nullable=True)
    experience_years = Column(Integer, nullable=True)
    consultation_fee = Column(Float, nullable=True)
    available_timeslots = Column(ARRAY(String), nullable=True)
