from pydantic import BaseModel, EmailStr, validator, Field, model_validator
from typing import Optional, List
from enum import Enum
from typing_extensions import Annotated
import re

class UserType(str, Enum):
    admin = "admin"
    doctor = "doctor"
    patient = "patient"

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    mobile: Annotated[str, Field(pattern=r"^\+88\d{11}$")]
    password: Annotated[str, Field(min_length=8)]
    user_type: UserType
    division: str
    district: str
    thana: str
    profile_image: Optional[bytes]
    license_number: Optional[str] = Field(None, description="Required for doctors")
    experience_years: Optional[int] = Field(None, description="Required for doctors")
    consultation_fee: Optional[float] = Field(None, description="Required for doctors")
    available_timeslots: Optional[List[str]] = Field(None, description="Required for doctors")

@validator("password")
def validate_password_strength(cls, v):
    pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if not re.match(pattern, v):
        raise ValueError("Password must be at least 8 characters, include 1 uppercase, 1 digit, 1 special character")
    return v


@model_validator(mode="after")
def validate_doctor_fields(cls, values):
    if values.get("user_type") == "doctor":
        required = ["license_number", "experience_years", "consultation_fee", "available_timeslots"]
        for field in required:
            if not values.get(field):
                raise ValueError(f"{field.replace('_', ' ').capitalize()} is required for doctors.")
    return values