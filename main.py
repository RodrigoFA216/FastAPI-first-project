#se importa fastapi desde la librería de fastapi
from fastapi import FastAPI

#se inicializa el servidor de fastapi en la variable app
app = FastAPI()
#modificación de la documentación
app.title="FastAPI para Machine learning"
app.version="0.0.1"

# se usa el decorador app para establecer una petición get 
# a la aplicación y se denota la direccion a la que se va a entrar '/'
# se define una función que va a tener como resultado un return con el string 'hello world'
@app.get('/', tags=['home'])
def message():
    return 'hello world'

developers=[
    {
        "id":1,
        "name": "Rodrigo",
        "lname": "Flores",
        "age": 24
    },
    {
        "id":2,
        "name": "Regina",
        "lname": "Luna",
        "age": 22
    },
    {
        "id":3,
        "name": "Rulas",
        "lname": "Raso",
        "age": 21
    },
    {
        "id":4,
        "name": "Eduardo",
        "lname": "Martinez",
        "age": 24
    },
    {
        "id":5,
        "name": "Rodrigo",
        "lname": "Flores",
        "age": 24
    }
]


@app.get('/test', tags=['test operation'])
def devs():
    return developers

@app.get('/get/params/{id}', tags=['test params'])
def params(id:int):#especifica el tipo de dato
    return id

@app.get('/params/filter/{id}', tags=['test params'])
def paramsFilter(id:int):
    for item in developers:
        if item['id']==id: return item
    return []

# parámetros query

@app.get('/params/filter/query/', tags=['test query'])
def paramsQuery(category:str):return category