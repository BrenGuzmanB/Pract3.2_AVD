"""
Created on Sun Dec  3 10:35:27 2023

@author: Bren Guzmán, Brenda García, María José Merino
"""

#%% LIBRERÍAS

from Correlation import graficar, subplot_graficas, pearson_coef
import pandas as pd
import matplotlib.pyplot as plt


#%% CARGAR ARCHIVO

df = pd.read_csv("kc_house_data.csv")
df = df.drop(['id', 'date'], axis=1)


#%% CORRELACIÓN ENTRE TODAS LAS VARIABLES

columnas = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
            'waterfront', 'view', 'condition', 'grade', 'sqft_above',
            'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode', 'lat', 'long',
            'sqft_living15', 'sqft_lot15','price']

# Inicializar el diccionario para almacenar los coeficientes y figuras
coeficientes_figuras = {}

# Generar gráficas de dispersión y calcular coeficientes de correlación
for i in range(len(columnas)):
    for j in range(i+1, len(columnas)):
        columna_x = columnas[i]
        columna_y = columnas[j]

        # Calcular el coeficiente de correlación
        coef_corr = pearson_coef(df[columna_x], df[columna_y])

        # Guardar en el diccionario
        key = (columna_x, columna_y)
        coeficientes_figuras[key] = (coef_corr)
        

#%% SUBPLOT PARA LAS VARIABLES CON MAYOR RELACIÓN (EN GENERAL)

# Ordenar el diccionario según los coeficientes de correlación de mayor a menor
coeficientes_ordenados = sorted(coeficientes_figuras.items(), key=lambda x: abs(x[1]), reverse=True)

# Seleccionar los 10 valores de correlación más altos
top_10_coeficientes = coeficientes_ordenados[:10]

# Inicializar una lista para almacenar las figuras
top_10_figuras = []

# Generar las figuras y almacenarlas en la lista
for par_columnas, coef_corr in top_10_coeficientes:
    figura = graficar(df, par_columnas[0], par_columnas[1])
    top_10_figuras.append(figura)

# Crear un subplot con las 10 figuras
subplot_graficas(top_10_figuras)


#%% SUBPLOT PARA LAS VARIABLES CON MAYOR RELACIÓN (CON LA VARIABLE OBJETIVO)

# Filtrar combinaciones que incluyen 'price'
combinaciones_con_price = [item for item in coeficientes_figuras.items() if 'price' in item[0]]

# Ordenar el diccionario según los coeficientes de correlación de mayor a menor
coeficientes_ordenados_price = sorted(combinaciones_con_price, key=lambda x: abs(x[1]), reverse=True)

# Seleccionar los 10 valores de correlación más altos
top_10_coeficientes_price = coeficientes_ordenados_price[:10]

# Inicializar una lista para almacenar las figuras
top_10_figuras_price = []

# Generar las figuras y almacenarlas en la lista
for (columna_x, columna_y), coef_corr in top_10_coeficientes_price:
    figura = graficar(df, columna_x, columna_y)
    top_10_figuras_price.append(figura)

# Crear un subplot con las 10 figuras
subplot_graficas(top_10_figuras_price)
  
  