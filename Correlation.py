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



# Función para generar un subplot
def subplot_graficas(axs):
    """
    Crea un subplot que muestra varias gráficas generadas con la función 'graficar'.

    Parámetros:
    - axs: Lista de ejes generados por la función 'graficar'.
    """
    num_graficas = len(axs)
    num_filas = (num_graficas // 2) + (num_graficas % 2)  # Calcula el número de filas para el subplot

    fig, axs_subplot = plt.subplots(num_filas, 2, figsize=(12, num_filas * 5))

    for i, ax in enumerate(axs):
        fila = i // 2
        columna = i % 2

        # Copiar el contenido del eje original al nuevo subplot
        axs_subplot[fila, columna].scatter(ax.collections[0].get_offsets()[:, 0], ax.collections[0].get_offsets()[:, 1])
        axs_subplot[fila, columna].plot(ax.lines[0].get_xdata(), ax.lines[0].get_ydata(), color='red', label='Regresión Lineal')

        # Configurar etiquetas y título
        axs_subplot[fila, columna].set_xlabel(ax.get_xlabel())
        axs_subplot[fila, columna].set_ylabel(ax.get_ylabel())
        axs_subplot[fila, columna].set_title(ax.get_title())

        # Mostrar la grilla
        axs_subplot[fila, columna].grid(True)

        correlacion = float(ax.get_legend().get_title().get_text().split()[-1])
        axs_subplot[fila, columna].legend(title=f'Coeficiente de Pearson: {correlacion:.2f}')

    plt.tight_layout()
    plt.show()
