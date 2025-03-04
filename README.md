# 4thewords_backend_mario_sepulveda
Backend project repository corresponding to the technical test for the fullstack developer position at 4THEWORDS.

# Commands to execute the development server (Backend)

## Crear entorno virtual en python
    python -m venv venv

## Ejecuta el entorno virtual de python 
    venv\Scripts\activate           (powershell windows)
    source venv/Scripts/activate    (linux/macOS)

## Instalar dependencias dentro del entorno virtual
    pip install fastapi uvicorn sqlmodel mysql-connector-python python-multipart

## Ejecuta el servidor de desarrollo de la API FastAPI
    uvicorn main:app --reload

## Desactiva en el entorno virtual de python
    deactivate

## Genera el archivo requirements.txt automáticamente
    pip freeze > requirements.txt

# API Version 0.0.1

# Keys Commits

* NF: new Feature
* CF: configuration file
* NC: new configuration
* UV: update version                




