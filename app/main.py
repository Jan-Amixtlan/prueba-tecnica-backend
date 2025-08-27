
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import services, contact, appointments

app = FastAPI(title="Cardan Is Leader In Auto Repair")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5180",
        "https://prueba-tecnica-frontend-iota.vercel.app"
    ],  # Permite peticiones desde Vercel
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(services.router, prefix="/services", tags=["Services"])
app.include_router(contact.router, prefix="/contact", tags=["Contact"])
app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Cardan Is Leader In Auto Repair"}
