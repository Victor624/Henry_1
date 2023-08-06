from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np
import zipfile




app = FastAPI(title='Proyecto Individual ',
            description='Victor Vargas',
            version='1.0.1')
# -------------------------------
@app.get("/", response_class=HTMLResponse, tags=['Index'])
async def read_index_html():
    """
    Ruta para el archivo index.html.
    """
    with open("index.html") as f:
        return f.read()
# ---------------------------------------------------
@app.get('/about/', tags=['Credits'])
async def about():
    """
    GET /about/

    Retorna un diccionario con información sobre el Primer Proyecto individual:  partime 01 de Data Science.
    """
    return {'message': 'Primer Proyecto individual:  partime 01 de Data Science'}

# Cargar los datasets
# ----------------------------------------------------
# Leer el archivo CSV
df = pd.read_csv('03 - DEF\Funcio.csv')
ml=pd.read_csv('04 - ML\Machine.csv')


# Definir la ruta de FastAPI
@app.get("/idioma/{x}")
def contar_peliculas(x: str):
    # Filtrar las películas según el idioma especificado en la URL
    peliculas = df.loc[df['original_language'] == x]
    
    # Obtener la cantidad de películas
    cant = len(peliculas)
    
    # Crear el mensaje de respuesta
    result = f"La cantidad de películas hechas con el idioma {x} es {cant}"
    
    # Retornar el mensaje de respuesta como un diccionario JSON
    return {"result": result}




@app.get("/peliculas_duracion/{x}")
def peliculas_duracion(x: str):
    x = x.lower().title()
    Pelicula = df['title']
    Cantidad = -1
    for i in Pelicula:
        Cantidad += 1
        if i == x:
            break
        else:
            Cantidad += 1
    Peli = df[["release_year", "runtime"]]
    Peli = pd.DataFrame(Peli)
    Peli = Peli.loc[Cantidad]
    resultado = f"La película <{x}> fue estrenada en: {Peli[0]} y tiene una duración de {Peli[1]} minutos"
    
    return {"resultado": resultado}


@app.get("/franquicias/{x}")
def franquicias(x: str):
    Franqui = df['name_prod']
    Cantidad = 0
    Cant_Peli = 0
    Ganancias = []
    total = sum(Ganancias)
    for i in Franqui:
        i = str(i)
        Cantidad += 1
        if x in i:
            Peli = df["Return"]
            Peli = pd.DataFrame(Peli)
            Peli = Peli.loc[Cantidad]
            Ganancias.append(Peli)
            Cant_Peli += 1
        
    if len(Ganancias) > 0:
        Ganancias = pd.DataFrame(Ganancias)
        Ganancias = Ganancias.dropna()
        Ganancias = Ganancias["Return"].replace(np.inf, 0)
        Ganancias = pd.DataFrame(Ganancias)
        suma = Ganancias["Return"].sum().round(2)
        result = f"La productora hizo {Cant_Peli} películas con una ganancia total de {suma.round(2)} y un promedio de {(suma/Cant_Peli).round(2)}"
    else:
        result = "No hay una productora con ese Nombre"
        
    return {"resultado": result}


@app.get("/peliculas/{x}")
def peliculas_pais(x: str):
    pais = df['name_Count']
    Lugar = 0
    Cant_Peli = 0
   
    for i in pais:
        i = str(i)
        Lugar += 1
        if x == i:
            Cant_Peli += 1
        
    if Cant_Peli > 0:       
        result = f"Se produjeron {Cant_Peli} películas en el país {x}"
    else:
        result = f"No se hicieron películas en el país {x}"
            
          
    return {"resultado": result}



@app.get("/productoras/{x}")
def productoras_exitosas(x: str):
    Franqui = df['name_prod']
    Cantidad = 0
    Cant_Peli = 0
    revenue = []
    
    for i in Franqui:
        i = str(i)
        Cantidad += 1
        if x in i:
            Peli = df["revenue"]
            Peli = pd.DataFrame(Peli)
            Peli = Peli.loc[Cantidad]
            revenue.append(Peli)
            Cant_Peli += 1
        
    if len(revenue) > 0:
        revenue = pd.DataFrame(revenue)
        revenue = revenue.dropna()
        revenue = revenue["revenue"].replace(np.inf, 0)
        revenue = pd.DataFrame(revenue)
        suma = revenue["revenue"].sum().round(2)
        result = f"La productora hizo {Cant_Peli} películas con un revenue total de {suma.round(2)}"
    else:
        result = "No hay una productora con ese nombre"
            
          
    return {"resultado": result}


@app.get("/directores/{x}")
def directores(x: str):
    Direct = df['Director']
    titl = []
    posi = -1
    
    for i in Direct:
        i = str(i)
        posi += 1
        if x in i:           
            title = df[["title", "release_date", "revenue", "Return"]]
            title = pd.DataFrame(title)
            title = title.loc[posi]
            titl.append(title)
        else:
            pass
    
    Lista = pd.DataFrame(titl)
    Lista = Lista.sort_values("Return", ascending=False)
   
    
    return {"directores": Lista.to_dict(orient="records")}  



@app.get("/peliculas_recomendadas/{pelicula}")
def peliculas_recomendadas(pelicula: str):




    # archivo CSV con los datos
    ML_DF1 = ml

    # Buscar la película por título en la columna 'title'
    movie = ML_DF1[ML_DF1['title'] == pelicula]

    if len(movie) == 0:
        return "La película no se encuentra en la base de datos."

    # Obtener el género y la popularidad de la película
    movie_genero = movie['name_genres'].values[0]
    movie_popularity = movie['popularity'].values[0]

    # matriz de características para el modelo de vecinos más cercanos
    features = ML_DF1[['popularity']]
    genres = ML_DF1['name_genres'].str.get_dummies(sep=' ')
    features = pd.concat([features, genres], axis=1)

    # Manejar valores faltantes (NaN) reemplazándolos por ceros
    features = features.fillna(0)

    # modelo de vecinos más cercanos
    nn_model = NearestNeighbors(n_neighbors=6, metric='euclidean')
    nn_model.fit(features)

    # Encontrar las películas más similares (excluyendo la película de consulta indicada por usuario)
    _, indices = nn_model.kneighbors([[movie_popularity] + [0] * len(genres.columns)], n_neighbors=6)
    similar_movies_indices = indices[0][1:]  # Excluyendo la primera película que es la misma consulta
    Pelis_recom = ML_DF1.iloc[similar_movies_indices]['title']

    # Si la película de consulta está en la lista de recomendaciones, la eliminamos
    if pelicula in Pelis_recom.tolist():
        Pelis_recom = Pelis_recom[Pelis_recom != pelicula]
 
    return Pelis_recom(pelicula)






















# Ejecutar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
