# 4thewords_backend_mario_sepulveda
Backend project repository corresponding to the technical test for the fullstack developer position at 4THEWORDS.

# Commands to execute the development server (Backend)

## Create virtual env in python
    python -m venv venv

## Execute the virtual env of python 
    venv\Scripts\activate           (powershell windows)
    source venv/Scripts/activate    (linux/macOS)

## Conecting to DB
### you must create a file .env in your project root and complete the values with your own values
~~~
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=the_name_of_db
~~~

## Install dependencies into virtual env
    pip install fastapi uvicorn sqlmodel mysql-connector-python python-multipart

## Execute the development server for API wiht FastAPI
    uvicorn main:app --reload

## Ejecuta la api por defecto en el puero execute API on port 8080
    uvicorn main:app --host 0.0.0.0 --port 8080 --reload

## disable virtual env
    deactivate

## Generates the requirements.txt file automatically
    pip freeze > requirements.txt

# API Version 1.2.5


# Keys Commits

* NF: new Feature
* CF: configuration file
* NC: new configuration
* UV: update version
* AR: add resources
* BF: bug fixed                




