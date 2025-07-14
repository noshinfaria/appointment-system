from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.db.database import get_db
from app.models import user as user_model
from app.core.security import get_password_hash, create_access_token, validate_password, validate_image

router = APIRouter()

@router.post("/register")
def register(user: UserCreate = Depends(), profile_image: UploadFile = File(None), db: Session = Depends(get_db)):
    if db.query(user_model.User).filter(
        (user_model.User.email == user.email) | (user_model.User.mobile == user.mobile)
    ).first():
        raise HTTPException(status_code=400, detail="Email or mobile already registered")

    image_path = None
    if profile_image:
        content = profile_image.file.read()
        try:
            validate_image(content, profile_image.content_type)
        except ValueError as ve:
            raise HTTPException(status_code=400, detail=str(ve))
        # Simulate saving the image
        image_path = f"uploads/{profile_image.filename}"
        with open(image_path, "wb") as f:
            f.write(content)

    timeslot_list = user.available_timeslots or []

    

    new_user = user_model.User(
        full_name=user.full_name,
        email=user.email,
        mobile=user.mobile,
        password=get_password_hash(user.password),
        user_type=user.user_type,
        division=user.division,
        district=user.district,
        thana=user.thana,
        profile_image=image_path,
        license_number=user.license_number,
        experience_years=user.experience_years,
        consultation_fee=user.consultation_fee,
        available_timeslots=timeslot_list,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"success": True, "message": "User registered successfully."}

@router.post("/login")
def login(form_data: dict, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.email == form_data["email"]).first()
    if not user or not validate_password(form_data["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}