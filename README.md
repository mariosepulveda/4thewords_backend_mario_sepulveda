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

## Ejecuta la api por defecto en el puero 8080
    uvicorn main:app --host 0.0.0.0 --port 8080 --reload

## Desactiva en el entorno virtual de python
    deactivate

## Genera el archivo requirements.txt automáticamente
    pip freeze > requirements.txt

# API Version 1.1.3

# Keys Commits

* NF: new Feature
* CF: configuration file
* NC: new configuration
* UV: update version
* AR: Add resources                




