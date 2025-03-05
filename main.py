from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles # para servir archivo estáticos
import uvicorn
import models
from database import engine
from routes import router
from fastapi.middleware.cors import CORSMiddleware
import os


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Leyendas", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permite peticiones desde React
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos los headers
)

# Asegurarte de que la carpeta 'uploads' existe
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Servir los archivos de la carpeta 'uploads'
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)