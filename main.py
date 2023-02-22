#se importa fastapi desde la librería de fastapi
from fastapi import FastAPI, Body, Request, Response
import math

#se inicializa el servidor de fastapi en la variable app
app = FastAPI()
#modificación de la documentación
app.title="FastAPI para Machine learning"
app.version="0.0.1"

developers=[
    {
        "id":1,
        "name": "Rodrigo",
        "lname": "Flores",
        "age": 24,
        "tech": "Python"
    },
    {
        "id":2,
        "name": "Regina",
        "lname": "Luna",
        "age": 22,
        "tech": "JavaScript"
    },
    {
        "id":3,
        "name": "Rulas",
        "lname": "Raso",
        "age": 21,
        "tech": "Matlab"
    },
    {
        "id":4,
        "name": "Eduardo",
        "lname": "Martinez",
        "age": 24,
        "tech": "CSS"
    },
    {
        "id":5,
        "name": "Rodrigo",
        "lname": "Flores",
        "age": 24,
        "tech": "DuplicateElement"
    }
]
#------------------------------------------------------------------------------
#---------------------------------MÉTODO GET-----------------------------------
#------------------------------------------------------------------------------

# se usa el decorador app para establecer una petición get 
# a la aplicación y se denota la direccion a la que se va a entrar '/'
# se define una función que va a tener como resultado un return con el string 'hello world'
@app.get('/', tags=['home'])
def message():
    return developers



@app.get('/test', tags=['test operation'])
def devs():
    return [{"mesage": "Working clean"}]


# Parámetros (sirve para recibir datos por URL) "/endpoint/{param}"
# Se especifica un parámetro que se va a recibir mediante la URL
# FastAPI detecta el parametro que se obtiene en el endpoint
# corresponde a un parámetro, este parámetro debe ser especificado 
# en la función como un parámetro de la misma junto con su tipo de dato
@app.get('/get/params/{id}', tags=['test params'])
def params(id:int):#especifica el tipo de dato
    return id

@app.get('/params/select/{id}', tags=['test params'])
def paramsFilter(id:int):
    return [item for item in developers if item['id']==id]

# Parámetros query (sirve para filtrar datos) "/endpoint/"
# Cuando no se especifica un parametro en el endpoint 
# FastAPI detecta el parametro que se pasa en la función 
# corresponde a un parámetro query en el endpoint 
# elparámetro de la función debe ser especificado con el tipo de dato
@app.get('/params/filter/query/', tags=['test query'])
def paramsQuery(query:str):return query

# Recibir más de un parámetro query en el endpoint
# se va a recibir como:
#       /params/query/Tech=Something&Age=Something
@app.get('/params/query/', tags=['test query'])
def searchQuery(Tech:str, Age:int):
    return [dev for dev in developers if dev['tech']==Tech and dev['age']==Age]

class Neurona:
    def __init__(self, w1, w2, theta):
        self.w1 = w1
        self.w2 = w2
        self.theta = theta

    def activacion(self, x1, x2):
        z = (self.w1 * x1) + (self.w2 * x2) - self.theta
        y = 1 / (1 + math.exp(-z))
        return y

@app.post('/ML/neurona/', tags=['Neurona'])
def neurona(theta:float=Body(), w1:float=Body(), w2:float=Body(), x1:float=Body(), x2:float=Body()):
    z=(w1*x1)+(w2*x2) -theta
    y=1 / (1 + math.exp(-z))
    n=Neurona(w1,w2,theta)
    res=n.activacion(x1,x2)
    if y:
        return [{"success": y},{"success": res},]
    else:
        return [{"message": "Error"}]


#------------------------------------------------------------------------------
#---------------------------------MÉTODO POST----------------------------------
#------------------------------------------------------------------------------

# Para evitar que los detecte como parámetros hay que agregar la clse Body() a 
# cada parámetro para especificar quienes son parámetros de endpoint y quienes 
# son parámetros de body. Adicionalmente se puede introducir a Body() 
# default=something respetando el tipo de dato para evitar errores
@app.post('/devs/', tags=['post elements'])
def devs(id:int=Body(), name:str=Body(), lname:str=Body(), age:int=Body(), tech:str=Body()):
    #recoje los IDs de developers para cotejar repeticiones
    ids=[ident["id"] for ident in developers]
    if id in ids:
        return [{"message": "ID repetido"}]
    else:
        developers.append({
            "id":id,
            "name": name,
            "lname": lname,
            "age": age,
            "tech": tech
        })
        return [{
            "id":id,
            "name": name,
            "lname": lname,
            "age": age,
            "tech": tech
        },]