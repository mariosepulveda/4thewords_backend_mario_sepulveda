from sqlalchemy.orm import Session
from models import Leyenda
from schemas import LeyendaCreate, LeyendaUpdate

def get_leyendas(db: Session):
    return db.query(Leyenda).all()

def get_leyenda(db: Session, leyenda_id: int):
    return db.query(Leyenda).filter(Leyenda.id == leyenda_id).first()

def create_leyenda(db: Session, leyenda: LeyendaCreate):
    db_leyenda = Leyenda(**leyenda.dict())
    db.add(db_leyenda)
    db.commit()
    db.refresh(db_leyenda)
    return db_leyenda

def update_leyenda(db: Session, leyenda_id: int, leyenda: LeyendaUpdate):
    db_leyenda = db.query(Leyenda).filter(Leyenda.id == leyenda_id).first()
    if db_leyenda:
        for key, value in leyenda.dict().items():
            setattr(db_leyenda, key, value)
        db.commit()
        db.refresh(db_leyenda)
    return db_leyenda

def delete_leyenda(db: Session, leyenda_id: int):
    db_leyenda = db.query(Leyenda).filter(Leyenda.id == leyenda_id).first()
    if db_leyenda:
        db.delete(db_leyenda)
        db.commit()
    return db_leyenda
