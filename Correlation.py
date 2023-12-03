"""
Created on Fri Dec  1 22:25:12 2023

@author: Bren Guzmán, Brenda García, María José Merino.
"""

# Función para calcular la correlación de Pearson
def pearson_coef(x, y):
   
    # Calcular las medias 
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    # Calcular el numerador y denominador
    numerador = sum((x - mean_x) * (y - mean_y) for x, y in zip(x, y))
    denominador = (sum((xi - mean_x)**2 for xi in x) * sum((yi - mean_y)**2 for yi in y))**0.5

    # Calcular el coeficiente de correlación de Pearson
    correlacion = numerador / denominador if denominador != 0 else 0

    return correlacion

# Función para graficar los puntos de dos variables aleatorias
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def graficar(df, columna_x, columna_y):
    """
    Genera una gráfica de dispersión entre dos variables con regresión lineal.

    Parámetros:
    - df: DataFrame que contiene los datos.
    - columna_x: Nombre de la columna para el eje x.
    - columna_y: Nombre de la columna para el eje y.
    
    Retorna:
    - Los ejes de la gráfica
    """
    # Obtener los datos de las columnas
    x = df[columna_x]
    y = df[columna_y]

    # Crear el modelo de regresión lineal
    modelo = LinearRegression()

    # Ajustar el modelo a los datos
    x = np.array(x).reshape(-1, 1)
    y = np.array(y)
    modelo.fit(x, y)

    # Hacer predicciones usando el modelo
    y_pred = modelo.predict(x)

    # Calcular el coeficiente de correlación de Pearson
    correlacion = pearson_coef(x.flatten(), y)

    # Graficar los puntos y la recta de regresión
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Puntos')
    ax.plot(x, y_pred, color='red', label='Regresión Lineal')

    # Configurar etiquetas y título automáticamente
    ax.set_xlabel(columna_x)
    ax.set_ylabel(columna_y)
    ax.set_title(f'Relación {columna_x} y {columna_y}')
    
    # Mostrar el coeficiente de correlación en la leyenda
    ax.legend(title=f'Coeficiente de Pearson: {correlacion:.2f}')

    # Mostrar la grilla
    ax.grid(True)
    
    return ax


