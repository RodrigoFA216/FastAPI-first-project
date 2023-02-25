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

# Endpoints

## GET

- '/' 
    - Devuelve un json de una variable llamada Developers
- '/test'
    - Devuelve un json con el contenido 
        [{"mesage": "Working clean"}]
- '/get/params/:id'
    - Espera un número entero como parámetro en la ruta para regresarlo como respuesta en texto plano
- '/params/select/:id'
    - Espera un número entero como parámetro en la ruta para retornar el item de developers que tenga ese entero en la propiedad ID, si no existe ninguno regresa un string vacío
- '/params/filter/query'
    - recibe como query dos strings (Tech y Age) que filtra a los Developers según los que correspondan con esas dos condiciones, si ninguno coincide regresa un string vacío.

## POST

- '/devs/'
    - Recibe desde el body: ID, Name, Lname, Age y Tech, evalúaque el id no exista, si existe responde un jeson con un atributo message con la propiedad "ID repetido", en caso contrario, inserta el elemento en developers y regresa los datos en Json
- '/ML/neurona/'
    - Recibe desde el body: Theta, W1, W2, X1, y X2 para comparar el resultado de una clase y según la expresión con el fin de probar las limitaciones del metaframework y su uso de estructuras de datos
    
        1 / (1 + math.exp(-1*((w1*x1)+(w2*x2) -theta)))
    
- '/neighbors/'
    - Obiene un minimo y un máximo como flotantes por medio de un Body 
        - Genera datos y outliers de forma uniforme con el mínimo y máximo.
        - En base al modelo de Numpy LocalOutlierFactor estableciendo los vecinos ceercanos como 20 genera una detección de outliers
    - Regresa un Json con el siguiente contenido:
        - Training realdata son los datos que genera la dispersión de la generación normal de datos (matriz de 100*2)
        - Training Outliers son los outliers generados
        - Data trained es el conjunto de ambos en una unión, con este conjunto de datos se va a ajustar el modelo LocalOutlierFactor
        - Outliers detected son los puntos que están en Data Trained que son detectados como outliers dentro de la dispersión 
        - Estructura:
``` Javascript
    [
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
```