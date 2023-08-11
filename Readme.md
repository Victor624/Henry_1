<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Desarrollado por: Victor de la Merced Vargas`**</h1>


Este proyecto tiene como objetivo utilizar dos conjuntos de datos relacionados con películas y actores, llamados "movies_dataset" y "credits". A lo largo del proyecto, abordaremos tareas como ETL, EDA, Machine Learning y el despliegue de una aplicación.
 

<hr>  


## Enunciado del Proyecto
Empezaste a trabajar como **`Data Scientist`** en una start-up que provee servicios de agregación de plataformas de streaming. El mundo es bello y vas a crear tu primer modelo de ML que soluciona un problema de negocio: un sistema de recomendación que aún no ha sido puesto en marcha! 

Vas a sus datos y te das cuenta que la madurez de los mismos es poca (ok, es nula :sob:): Datos anidados, sin transformar, no hay procesos automatizados para la actualización de nuevas películas o series, entre otras cosas….  haciendo tu trabajo imposible :weary:. 

Debes empezar desde 0, haciendo un trabajo rápido de **`Data Engineer`** y tener un **`MVP`** (_Minimum Viable Product_) para el cierre del proyecto! Tu cabeza va a explotar 🤯, pero al menos sabes cual es, conceptualmente, el camino que debes de seguir :exclamation:. Así que te espantas los miedos y te pones manos a la obra :muscle:



# Diccionario de Carpetas y Archivos En Repositorio


    ⏩"00 - DATA": "En esta carpeta se guardan los archivos comprimidos de los archivos de Movies_Dataset.csv y 
                    credits.csv" con los cuales vamos a trabajar

    ⏩"01 - ETL": ""Contiene 5 carpetas que incluyen procesos de transformación y limpieza de datos, tratamiento de
	columnas anidadas, sustitución de valores nulos, revisión de tipos de datos y códigos para eliminar
	valores repetidos o con formatos distintos a los que corresponden en su columna:
                    01 - Fraccionado DataFrame
                    02 - Desanidado  de Columnas
                    03 - Armado de archivo completo
                    04 - Tratamiento de Datos Nulos
                    05 - Dataframe para operaciones
                    06 - Daraframe data para Funciones",

    ⏩"02 - EDA ": "Contiene el archivo con el que se realizó el análisis exploratorio de los datos.",

    ⏩"03 - DEF": "Genere las funciones necesarias para que nos requirieron en trabajo practico.",

    ⏩"04 - ML": "Archivo de Machine Learning"

    ⏩"Henry_1.zip": "Archivo comprimido en formato .zip que contiene la data limpia.",

    ⏩"main.py": "Archivo que contiene todo el código de la API desarrollada con FastAPI.",

    ⏩"requirements.txt": "Archivo útil para realizar el despliegue en Render."

## **Proceso de Trabajo**

A lo largo del proyecto afronte grandes desafios, como entablecer un pensamiento critico y la capacidad de autogestionarme y ser un autodidacta constante, busque, investigue, racionalice, consulte con por varios canales
para encontrar la mejor forma de plasmar todo aprendido.-

Mi repositorio se encuentra establecido de una manera que al descarlo puedan hacer un seguimiento de los procesos
y resultados conseguidos sobre los DataSet Originales.-

En resumen, este proyecto consegui  la autonomía, la organización, la resolución de problemas, la comunicación escrita, el aprendizaje autodirigido y el pensamiento crítico. 


# ETL y EDA

## Exploración y Limpieza de Datos


La exploracion de datos tuve que desarrolar un sistema donde nada quede librado al azar, donde una simple coma pueda arruinar mi proyecto entonces me enfoque en crear un sistema jerarguico en donde
cada paso que hiba a avanzando y tenia que retroceder para corregir algo, no perdia el camino 
recorrido solo vastaria ir a jupiter en donde tenia que hacer la correcion ejecutaba el cambio y se 
me hiban modificando los archivos consecuentes sin alterar todo lo hecho en el camino.-


Comence creando la carpeta    00 - DATA, ahi guardo los dataset originales de formato zip en donde de ahi empieza todo la limpieza.-

A continuacion cree la carpeta 01 - ETL en donde tambien hice sub-carpetas en donde hice en forma secuencial todo el ETL:


        01 - Fraccionando Daframe: En esta carpeta cree una jupyter para separa los datos para que nececito
        hacerle limpieza, que al darle arranque me divide lo que necesito, como el desanidado del dataset de
        movies y el de Credit, y me duvuelve dos csv que se guardaran en la carpeta siguiente para la siguiente
        transformacion.

        02 - Desanidado de Columnas: En esta carpeta cree dos Jupyter en donde los datos mediantes funciones que
        cree, pude hacer el desanidado en forma casi automatico, otorgandome tiempo y seguiridad a la hora de
        usarlos, de ellos tambien me duvuelve dos csv que se guardaran en la carpeta siguiente para la siguiente
        transformacion.-

        03 - Armado el Completo: En esta carpeta cree un Jupiter donde concatene los datos desencadenados y loS
        uni al dataset original haciendo asi un nuevo dataset, con el que puedo trabajar con los datos nulos Y
        variables inconsistente, lo hice de esta manera para no perder el Indice de todo el daset original.-

        04 - Tratamientos de Datos Nulos: En este Jupiter trate con todos los nulos rellené los valores nulos en
        los campos `revenue` y `budget` con el número 0. Esta acción me permitió manejar adecuadamente los datos
        faltantes y evitar posibles problemas en etapas posteriores del proyecto.
        
        Asimismo, eliminé los registros con valores nulos en el campo `release date` y aseguré que todas las
        fechas estén en el formato AAAA-mm-dd. Esta transformación fue esencial para analizar y comparar de
        manera efectiva las fechas de estreno de las películas.
        
        calculé un nuevo campo llamado `return`, el cual representa el retorno de inversión al dividir los campos
        `revenue` y `budget`. En casos donde no había datos disponibles para el cálculo, asigné el valor 0.
        
        creé una nueva columna llamada `release_year`, la cual me permitió extraer el año de lanzamiento de cada 
        película.
        Y tambien eliminé las columnas que no eran relevantes, tales como `video`, `imdb_id`, `adult`
        `original_title`, `poster_path` y `homepage`. Esta acción me permitió reducir el ruido en mis datos.-
        
        y tambien me duvuelve un csv que se guardaran en la carpeta siguiente para la siguiente transformacion.

        05 - Dataframe Para Operaciones: En esta carpeta cree un jupyter para separar solo la informacioN
        importante para Hacer el EDA, las Funciones y el Machine Learning y tambien como las otras devuelve.-
        
        06 - Dataset Para Funciones y EDA: Finalmente en esta carpeta guardo los dataset y de esta carpeta se van
        a desprender los archivos necesario para realizar el EDA, Funcione y Machine Learning.-     



## ---------------------------------------------------------------------------------------------------------------


## Diccionario de datos


Haber separado los datos en el ETL en diferentes conjuntos y crear diccionarios de datos para cada uno de ellos ha sido una decisión clave en mi proyecto individual de Ciencia de Datos. Esta estructura organizativa me ha brindado una serie de beneficios importantes.


A continuación se muestra un diccionario que describe cada columna en el conjunto de datos del archivo data_final.csv:

```python
column_description = {
    ['adult'
     'budget'
     'id'
     'imdb_id'
     'original_language'
     'overview'
     'popularity'
     'release_date'
     'revenue'
     'runtime'
     'status'
     'tagline',
     'title'
     'vote_average'
     'vote_count'
     'id.1'
     'Actor'
     'Director'
     'id_belong'
     'name_belong'
     'name_genres'
     'id_genres'
     'name_Spoken'
     'iso_639_1_Spoken'
     'id_prod'
     'name_prod'
     'iso_3166_1_Count'
     'name_Count
     'release_year'
     'Return'
}

```

A continuación se muestra un diccionario que describe cada columna en el conjunto de datos del archivo Funcio.csv:

```python
column_description = {
    'title'
    'original_language'
    'release_year'
    'name_belong'
    'runtime',
    'name_prod'
    'Return'
    'name_Count'
    'release_date'
    'revenue'
    'Return'
    'Director'
}

```

A continuación se muestra un diccionario que describe cada columna en el conjunto de datos del archivo Machine.csv:

```python
column_description = {
    'title'
    "name_genres"
    'popularity''
}
```


## s---------------------------------------------------------------------------------------------------------------

## Análisis Exploratorio de Datos (EDA) Carpeta 02 - EDA

Después de completar las tareas de limpieza de datos, realicé un análisis exploratorio exhaustivo utilizando técnicas estadísticas y visualizaciones. El archivo donde se llevó a cabo este análisis se encuentra en la carpeta "data_a_explorar", en un notebook que contiene las gráficas de exploración.

Durante el análisis exploratorio, utilicé las siguientes librerías: pandas, numpy, matplotlib.pyplot y seaborn. Estas herramientas me permitieron realizar diversas actividades, como calcular el porcentaje de valores faltantes en cada columna, filtrar las columnas con valores faltantes y examinar variables numéricas como "popularity", "vote_average", "vote_count", "runtime", "budget", "revenue" y "return".

También realicé cálculos de estadísticas descriptivas, como la media, mediana, desviación estándar y percentiles, para comprender la distribución de los datos. Generé histogramas y gráficos de caja para visualizar las variables numéricas, así como un gráfico de dispersión para analizar la relación entre los ingresos y presupuestos de las películas.

Además, realicé diversas visualizaciones para explorar la distribución de películas por mes y año de lanzamiento, los países con mayor producción cinematográfica, los géneros más populares a lo largo del tiempo, entre otros análisis. También generé un mapa de calor para examinar las relaciones entre las variables.

Este análisis exploratorio de datos fue fundamental para obtener conocimientos valiosos que nos ayudaron a comprender mejor el conjunto de datos y a tomar decisiones informadas en etapas posteriores del proyecto. Nos permitió descubrir patrones, identificar outliers y obtener una comprensión más profunda de las características de las películas y su éxito financiero.

# Funciones

## Desarrollo de Funciones (DEF) carpeta 03 - DEF


Deben crear 6 funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una .

                def peliculas_idioma( Idioma: str ): Esta Funcion devuelve el idioma Idioma solicitado y la
    cantidad de  peliculas hechas con ese idioma:

                    Ejemplo de retorno: X cantidad de películas fueron estrenadas en idioma

                def peliculas_duracion( Pelicula: str ): Se ingresa una pelicula. Debe devolver la duracion y el año. 
                    Ejemplo de retorno: X . Duración: x. Año: xx

                def franquicia( Franquicia: str ): Se ingresa la franquicia, retornando la cantidad de peliculas
    ganancia total y promedio
                    Ejemplo de retorno: La franquicia X posee X peliculas, una ganancia total de x y una ganancia promedio de xx

                def peliculas_pais( Pais: str ): Se ingresa un país , retornando la cantidad de peliculas
    producidas en el mismo.

                    Ejemplo de retorno: Se produjeron X películas en el país X

                def productoras_exitosas( Productora: str ): Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo.

                    Ejemplo de retorno: La productora X ha tenido un revenue de x

                def get_director( nombre_director ): Se ingresa el nombre de un director que se encuentre dentro
    de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el 
    nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en 
    formato lista.



# Sistema de Recomendación

## Desarrollo de Modelos de Machine Learning (ML) carpeta 04 - ML


Para el desarrollo del sistema de recomendación utile es elmétodo de los k vecinos más cercanos 
(en inglés: k-nearest neighbors, abreviadok-nn) es un método de clasificación supervisada (Aprendizaje,
 estimación basada en un conjunto de entrenamiento y prototipos) que sirve para estimar la función de densidad 

Este es un método de clasificación no paramétrico, que estima el valor de la función de densidad de probabilidad 
o directamente la probabilidad a posteriori de que un elemento x pertenezca a la clase 

 a partir de la información proporcionada por el conjunto de prototipos. En el proceso de aprendizaje no se hace ninguna suposición acerca de la distribución de las variables predictoras.

 En el reconocimiento de patrones, el algoritmo k-nn es usado como método de clasificación de objetos (elementos) 
 basado en un entrenamiento mediante ejemplos cercanos en el espacio de los elementos. 

k-nn es un tipo de aprendizaje vago (lazy learning), donde la función se aproxima solo localmente y todo el
 cómputo es diferido a la clasificación. La normalización de datos puede mejorar considerablemente la exactitud 
 del algoritmo.

## ---------------------------------------------------------------------------------------------------------------

# API con FASTAPI

## Desarrollo de la API

La API se desarrolló utilizando FastAPI, un framework web de Python que nos permite crear servicios web de manera rápida y eficiente. A continuación, se mencionan las librerías y frameworks utilizados en la creación de la API, junto con una breve descripción de su función y uso en el proyecto:

- `FastAPI`: FastAPI es un framework web de alto rendimiento basado en Python. Se utilizó para crear y gestionar la API, proporcionando rutas y controladores para las diferentes funciones y endpoints.
- `pandas`: pandas es una librería de Python ampliamente utilizada para la manipulación y análisis de datos. Se utilizó para cargar y procesar los conjuntos de datos, permitiendo realizar consultas y realizar operaciones sobre ellos.
- `zipfile`: zipfile es una librería de Python que permite trabajar con archivos comprimidos en formato ZIP. Se utilizó para descomprimir archivos ZIP que contenían los conjuntos de datos necesarios para la API.
- `sklearn.neighbors`: sklearn.neighbors es un módulo de la librería scikit-learn que contiene algoritmos de vecinos más cercanos (K-Nearest Neighbors). Se utilizó para implementar funcionalidades relacionadas con el sistema de recomendación, como encontrar vecinos más cercanos basados en características similares.

Cada una de estas librerías y frameworks desempeñó un papel crucial en el desarrollo de la API y permitió implementar diferentes funcionalidades, desde el procesamiento de datos hasta la creación de modelos de Machine Learning para el sistema de recomendación. Su uso combinado proporcionó las herramientas necesarias para construir una API robusta y funcional.



# Deployment

## Despliegue (Deployment)

Para el despliegue de la API en Render, se creó un archivo llamado `requirements.txt`. Este archivo es utilizado para especificar las dependencias y las versiones exactas de las librerías que son necesarias para que la API funcione correctamente.

Render utiliza el archivo `requirements.txt` para instalar automáticamente las dependencias especificadas en el entorno de ejecución de la aplicación. Al incluir las dependencias y las versiones adecuadas en este archivo, se asegura que la API pueda ejecutarse sin problemas en Render, con todas las bibliotecas necesarias correctamente instaladas.

Cada línea del archivo especifica el nombre de una librería seguido de `==` y la versión requerida. Pueden incluirse tantas líneas como sean necesarias para todas las dependencias de la API.

Una vez que el archivo `requirements.txt` está correctamente configurado, Render utilizará esta información para instalar automáticamente las librerías necesarias durante el proceso de despliegue de la API. Esto asegura que todas las dependencias estén disponibles en el entorno de ejecución de la aplicación en Render.

<a href="https://trabajo-vargas-victor.onrender.com/docs#" target="_blank">Mi Aplicacion</a>

<a href="https://trabajo-vargas-victor.onrender.com/" target="_blank">Mi Aplicacion</a>


