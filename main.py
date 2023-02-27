#se importa fastapi desde la librería de fastapi
from fastapi import FastAPI, Body, Request, Response
# Esquemas
from pydantic import BaseModel, Field
from typing import Optional
# Para la neurona
import math

# Análisis numérico
import numpy as np
from sklearn.neighbors import LocalOutlierFactor
import matplotlib.pyplot as plt

#se inicializa el servidor de fastapi en la variable app
app = FastAPI()
#modificación de la documentación
app.title="FastAPI para Machine learning"
app.version="0.0.1"

class Developer(BaseModel):
    id:int | None = None
    name:str | None = Field(max_length=10)
    lname:str | None = None
    age:int | None = 18
    tech: Optional[str] =None

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

#------------------------------------------------------------------------------
#---------------------------------MÉTODO PUT-----------------------------------
#------------------------------------------------------------------------------

@app.put('/developers/{id}', tags=['put method'])
def update_dev(id:int, name:str=Body(), lname:str=Body(), age:int=Body(), tech:str=Body()):
    print('hola')
    for developer in developers:
        if developer['id']==id:
            developer['name']=name
            developer['lname']=lname
            developer['age']=age
            tech = ' '+tech
            developer['tech']+=tech
            return developers

#------------------------------------------------------------------------------
#---------------------------------MÉTODO DEL-----------------------------------
#------------------------------------------------------------------------------

@app.delete('/developers/{id}', tags=['delete method'])
def delete_dev(id:int):
    for developer in developers:
        if developer['id']==id:
            developers.remove(developer)
            return developers
    




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
#---------------------------------Detect Density-------------------------------
#------------------------------------------------------------------------------

@app.post('/neighbors/', tags=['Detect Density'])
def detectFunction(min:float=Body(),max:float=Body()):
    # Generar datos sintéticos
    np.random.seed(42) #numpy configura la generación de datos random con una semilla 42
    X = 0.3 * np.random.randn(100, 2) # genera datos de 100 filas por dos columnas
    #genera datos que funcionarán de outliers entre -4 y 4 de 20 filas y dos columnas
    X_outliers = np.random.uniform(low=(min*-1), high=(max*2), size=(20, 2)) 
    # concatenamos en x las matrices que ya habíamos hecho, 
    # en primer lugar concatenamos x desplazado en 2 y x desplazado en -2 (en y) y concatenamos los outliers 
    # esto va a generar una dispersión atípica de los valores outliers
    # no importa el orden en que sean concatenados mientras estén en un solo objeto
    x = np.r_[X + (max), X - (min), X_outliers]

    # Ajustar el modelo de detección de outliers
    # crea un objeto del modelo de detección basado en densidad llamado LocalOutlierFactor
    # un punto es considerado un outlier si su densidad de vecinos es muy baja en comparación 
    # con la densidad de los vecinos de los demás puntos
    # La variable n_neighbors se utiliza para especificar el número de vecinos más cercanos que 
    # se utilizarán para calcular la densidad
    clf = LocalOutlierFactor(n_neighbors=20)
    y_pred = clf.fit_predict(x)
    #opción 1
    y_predict_dict = {i: x.tolist() for i, x in enumerate(y_pred) if x.tolist()==-1}
    y_pred_list = y_pred.tolist()
    outlierdict = {}
    x_first=x[:,0]
    x_second=x[:,1]
    for key, value in y_predict_dict.items():
        local=int(key)
        matrixX=x_first[local]
        matrixY=x_second[local]
        outlierdict.update({str(matrixX): matrixY})
    print("outlierdict", outlierdict)
    print("y_pred", y_pred)
    return [
        {
            "message": "success",
            "processed": True
        },
        {
            "Training realdata": [X],
            "Training Outliers": [X_outliers]
        },
        {
            "Data Trained": [x]
        },
        {
            "Outliers detected": outlierdict
        }
    ]