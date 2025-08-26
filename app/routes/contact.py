from fastapi import APIRouter

router = APIRouter()

@router.post("/api/v1/contact/")
def send_contact_form():
    return {"message": "Formulario de contacto recibido"}
