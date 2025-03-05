from fastapi import APIRouter, Depends, HTTPException, Form, File, UploadFile
from sqlalchemy.orm import Session
from datetime import datetime
import shutil
import crud, schemas, database
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Asegurar que la carpeta exista

#enpoint para listar todas las leyendas
@router.get("/leyendas", response_model=list[schemas.LeyendaResponse])
def get_leyendas(db: Session = Depends(database.get_db)):
    return crud.get_leyendas(db)


#endpoint para buscar una leyenda por su id
@router.get("/leyendas/{leyenda_id}", response_model=schemas.LeyendaResponse)
def get_leyenda(leyenda_id: int, db: Session = Depends(database.get_db)):
    leyenda = crud.get_leyenda(db, leyenda_id)
    if not leyenda:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    return leyenda


#endpoint para crear una leyenda
@router.post("/leyendas", response_model=schemas.LeyendaResponse)
def create_leyenda(
    nombre: str = Form(...),
    descripcion: str = Form(...),
    categoria: str = Form(...),
    provincia: str = Form(...),
    canton: str = Form(...),
    distrito: str = Form(...),
    imagen: UploadFile = File(...),
    db: Session = Depends(database.get_db)
):
    # Guardar la imagen
    file_path = f"{UPLOAD_DIR}/{imagen.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(imagen.file, buffer)

    # Crear objeto de leyenda
    leyenda_data = schemas.LeyendaCreate(
        nombre=nombre,
        descripcion=descripcion,
        categoria=categoria,
        provincia=provincia,
        canton=canton,
        distrito=distrito,
        imagen_url=file_path  # Guardar la URL en la BD
    )

    return crud.create_leyenda(db, leyenda_data)


#enpoint para editar una leyenda
@router.put("/leyendas/{leyenda_id}", response_model=schemas.LeyendaResponse)
def update_leyenda(leyenda_id: int, leyenda: schemas.LeyendaUpdate, db: Session = Depends(database.get_db)):
    updated = crud.update_leyenda(db, leyenda_id, leyenda)
    if not updated:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    return updated


#enpoint para eliminar una leyenda
@router.delete("/leyendas/{leyenda_id}")
def delete_leyenda(leyenda_id: int, db: Session = Depends(database.get_db)):
    deleted = crud.delete_leyenda(db, leyenda_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    return {"message": "Leyenda eliminada"}
