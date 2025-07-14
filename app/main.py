from fastapi import FastAPI
from app.api import auth, address #, users, doctors, appointments

app = FastAPI(
    title="Appointment Booking System",
    description="This API allows patients to book appointments, doctors to manage schedules, and admins to generate reports.",
    version="1.0.0",
    contact={
        "name": "Support Team",
        "email": "support@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(address.router, prefix="/address", tags=["Address"])
# app.include_router(users.router, prefix="/users", tags=["Users"])
# app.include_router(doctors.router, prefix="/doctors", tags=["Doctors"])
# app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])
