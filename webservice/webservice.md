# WebService
Esta carpeta contiene el árbol de carpetas necesario para poder crear un servicio *REST* que permita operaciones *CRUD* en la base de datos a otras personas. Esto convierte el proyecto en colaborativo.

Para la realización de este TFM no he incorporado seguridad al proyecto por falta de tiempo, pero un proyecto real debe incorporar un módulo que permita la creación y mantenimiento de cuentas de usuario autorizadas a acceder al servicio.

Este proyecto tampoco incorpora una capa SSL para proteger la conexión TCP/IP, que sería imprescindible en el mundo real.

## Estructura
Para la realización del webservice he elegido el framework **FastAPI**

Una aplicación FastAPI contiene el siguiente árbol de directorios

``` .
└── variants_app
    ├── __init__.py
    ├── crud.py
    ├── database.py
    ├── main.py
    ├── models.py
    └── schemas.py
```
- **\_\_init\_\_.py** es un archivo vacío que solo sirve para que Python sepa que variants_app es un package.
- **crud.py** contiene funciones para interactuar con la base de datos haciendo operaciones CRUD
- **database.py** implementa SQLAlchemy y establece la conexión a la DB
- **main.py** implementa SQLAlchemy y hace uso del resto de módulos de la app. Su ejecución crea la estructura de tablas en la DB
- **models.py** implementa SQLAlchemy y crea las clases que abstraen las tablas de la DB en objetos utilizables
- **schemas.py** implementa Pydantic y crea el modelo de datos

## Dependencias
Un proyecto FastAPI con acceso a DB tiene las siguientes dependencias.
- [Starlette](https://www.starlette.io/) para la parte web
- [Pydantic](https://docs.pydantic.dev/) para los datos
- Una base de datos con conector para python (SQLite en este caso, pero puede ser cualquiera)
- [SQLAlchemy](https://www.sqlalchemy.org/)

## Funcionamiento
Para arrancar el servicio basta con ejecutar

```uvicorn variants_app.main:app --reload```

El webservice será accesible desde la dirección

```http://127.0.0.1:8000```

Como hemos indicado antes, se trata de un entorno de desarrollo y no hay que permitir el tráfico exterior a la red local por seguridad.

## Utilización
Para consumir los servicios ofrecidos por la aplicación web hay que acceder a los endpoints correspondientes con cualquier cliente. Cualquier navegador podría servir, ya que al no necesitar autentificación cualquiera tiene acceso. También se pueden usar Postman, Insomnia o desde la linea de comandos, CURL o la consola de Python.
