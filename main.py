from fastapi import FastAPI
import models
from database import engine
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Leyendas", version="1.0")

app.include_router(router, prefix="/api")
