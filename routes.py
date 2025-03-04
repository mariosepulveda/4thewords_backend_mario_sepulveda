from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, database

router = APIRouter()

@router.get("/leyendas", response_model=list[schemas.LeyendaResponse])
def get_leyendas(db: Session = Depends(database.get_db)):
    return crud.get_leyendas(db)

@router.get("/leyendas/{leyenda_id}", response_model=schemas.LeyendaResponse)
def get_leyenda(leyenda_id: int, db: Session = Depends(database.get_db)):
    leyenda = crud.get_leyenda(db, leyenda_id)
    if not leyenda:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    return leyenda

@router.post("/leyendas", response_model=schemas.LeyendaResponse)
def create_leyenda(leyenda: schemas.LeyendaCreate, db: Session = Depends(database.get_db)):
    return crud.create_leyenda(db, leyenda)

@router.put("/leyendas/{leyenda_id}", response_model=schemas.LeyendaResponse)
def update_leyenda(leyenda_id: int, leyenda: schemas.LeyendaUpdate, db: Session = Depends(database.get_db)):
    updated = crud.update_leyenda(db, leyenda_id, leyenda)
    if not updated:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    return updated

@router.delete("/leyendas/{leyenda_id}")
def delete_leyenda(leyenda_id: int, db: Session = Depends(database.get_db)):
    deleted = crud.delete_leyenda(db, leyenda_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    return {"message": "Leyenda eliminada"}
