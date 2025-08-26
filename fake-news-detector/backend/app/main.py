# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router as api_router

app = FastAPI(title="Fake News Detection API")

# Permitir solicitudes desde cualquier origen (útil para pruebas)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir las rutas del archivo api.py
app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "🚀 API de detección de noticias falsas activa"}
