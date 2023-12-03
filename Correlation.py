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
