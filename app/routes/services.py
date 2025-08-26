from fastapi import APIRouter

router = APIRouter()
# En tus archivos routes/
@router.get("/api/v1/services/")
@router.get("/api/v1/services/{service_id}")
@router.post("/api/v1/services/")

@router.get("/api/v1/technicians/")
@router.get("/api/v1/technicians/{technician_id}")

@router.post("/api/v1/contact/")
@router.post("/api/v1/reviews/")
@router.get("/api/v1/reviews/")

@router.post("/api/v1/appointments/")
@router.get("/api/v1/appointments/")

@router.get("/api/v1/stats/")

@router.post("/api/v1/newsletter/subscribe/")
def subscribe_newsletter():
	return {"message": "Suscripción exitosa"}