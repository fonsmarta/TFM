# WebService
Esta carpeta contiene el árbol de carpetas necesario para poder crear un servicio *REST* que permita operaciones *CRUD* en la base de datos a otras personas. Esto convierte el proyecto en colaborativo.
Para la realización de este TFM no he incorporado seguridad al proyecto por falta de tiempo, pero un proyecto real debe incorporar un módulo que permita la creación y mantenimiento de cuentas de usuario autorizadas a acceder al servicio.
Este proyecto tampoco incorpora una capa SSL para proteger la conexión TCP/IP, que sería imprescindible en el mundo real.

## Estructura
Para la realización del webservice he elegido el framework **FastAPI**
Una aplicación FastAPI contiene el siguiente árbol de directorios

## Dependencias
Un proyecto FastAPI con acceso a DB tiene las siguientes dependencias.
- Usa (Starlette)[https://www.starlette.io/] para la parte web
- Usa (Pydantic)[https://docs.pydantic.dev/] para los datos
- Una base de datos con conector para python (SQLite en este caso, pero puede ser cualquiera)
- Usa (SQLAlchemy)[https://www.sqlalchemy.org/]

## Funcionamiento
Para arrancar el servicio basta con ejecutar
```uvicorn sql_app.main:app --reload```
El webservice será accesible desde la dirección
