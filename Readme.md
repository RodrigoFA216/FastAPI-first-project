# Requerimientos

- python v3^
- conocimientos en python

# Del proyecto
## disposición del servidor:

uvicorn 'archivo':'función'

    uvicorn main:app

Se puede disponer en un puerto específico como el 2300 con el comando:

    uvicorn main:app --port 2300

Para poder reiniciar el servidor co los cambios automáticamente se usa:

    uvicorn main:app --reload

Se puede dejar disponible para todos los dispositivos en la misma red con el comando:

    uvicorn main:app --host 0.0.0.0