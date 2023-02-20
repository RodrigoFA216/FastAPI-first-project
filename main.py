#se importa fastapi desde la librería de fastapi
from fastapi import FastAPI

#se inicializa el servidor de fastapi en la variable app
app = FastAPI()

# se usa el decorador app para establecer una petición get 
# a la aplicación y se denota la direccion a la que se va a entrar '/'
# se define una función que va a tener como resultado un return con el string 'hello world'
@app.get('/')
def message():
    return 'hello world'