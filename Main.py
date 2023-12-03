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
        
    