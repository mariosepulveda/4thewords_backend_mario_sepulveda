from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LeyendaBase(BaseModel):
    nombre: str
    descripcion: str
    categoria: str
    provincia: str
    canton: str
    distrito: str
    imagen_url: Optional[str] = None
    fecha_creacion: Optional[datetime]  # Permitir valores opcionales y tipo datetime


class LeyendaCreate(LeyendaBase):
    fecha_creacion: Optional[datetime] = datetime.utcnow()  # Agregar fecha por defecto

class LeyendaUpdate(LeyendaBase):
    fecha_creacion: Optional[datetime]  # Permitir actualización de fecha

class LeyendaResponse(LeyendaBase):
    id: int
    fecha_creacion: datetime  # Incluirlo en la respuesta

    class Config:
        from_attributes = True
