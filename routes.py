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
@router.put("/leyendas/{id}", response_model=schemas.LeyendaResponse)
def update_leyenda(
    id: int,
    nombre: str = Form(None),
    descripcion: str = Form(None),
    categoria: str = Form(None),
    provincia: str = Form(None),
    canton: str = Form(None),
    distrito: str = Form(None),
    imagen: UploadFile = File(None),  # Imagen opcional
    db: Session = Depends(database.get_db)
):
    # Obtener la leyenda existente
    leyenda_actual = crud.get_leyenda(db, id)
    if not leyenda_actual:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")

    # Si se envía una nueva imagen, guardarla y reemplazar la anterior
    imagen_url = leyenda_actual.imagen_url  # Mantener la imagen actual si no se cambia
    if imagen:
        file_path = f"{UPLOAD_DIR}/{imagen.filename}"
        
        # Borrar imagen anterior si existía
        if os.path.exists(leyenda_actual.imagen_url):
            os.remove(leyenda_actual.imagen_url)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(imagen.file, buffer)
        
        imagen_url = file_path

    # Crear objeto de actualización con los datos enviados (solo si no son `None`)
    update_data = {}
    if nombre is not None:
        update_data["nombre"] = nombre
    if descripcion is not None:
        update_data["descripcion"] = descripcion
    if categoria is not None:
        update_data["categoria"] = categoria
    if provincia is not None:
        update_data["provincia"] = provincia
    if canton is not None:
        update_data["canton"] = canton
    if distrito is not None:
        update_data["distrito"] = distrito
    if imagen_url is not None:
        update_data["imagen_url"] = imagen_url

    # Actualizar la leyenda en la BD
    updated_leyenda = crud.update_leyenda(db, id, update_data)

    return updated_leyenda


#enpoint para eliminar una leyenda
@router.delete("/leyendas/{leyenda_id}")
def delete_leyenda(leyenda_id: int, db: Session = Depends(database.get_db)):
    deleted = crud.delete_leyenda(db, leyenda_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    return {"message": "Leyenda eliminada"}
