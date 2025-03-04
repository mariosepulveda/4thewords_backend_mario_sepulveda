from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LeyendaBase(BaseModel):
    titulo: str
    descripcion: str
    origen: str
    imagen_url: Optional[str] = None

class LeyendaCreate(LeyendaBase):
    pass

class LeyendaUpdate(LeyendaBase):
    pass

class LeyendaResponse(LeyendaBase):
    id: int
    fecha_creacion: datetime

    class Config:
        from_attributes = True
