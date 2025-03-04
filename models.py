from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime

class Leyenda(Base):
    __tablename__ = "leyendas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    origen = Column(String(255), nullable=False)
    imagen_url = Column(String(255), nullable=True)
