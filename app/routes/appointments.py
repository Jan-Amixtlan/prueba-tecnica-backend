from fastapi import APIRouter

router = APIRouter()

@router.post("/api/v1/appointments/")
def create_appointment():
    return {"message": "Cita creada exitosamente"}
