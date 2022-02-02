# Ejercicio 1
# Enunciado: Imprime todos los ficheros existentes en tu carpeta de Descargas
# Objetivo:
# - Aprender a utilizar librerías sencillas (en este caso, os) y sus funciones.
# - Aprender a utilizar los bucles y los condicionales.
# El algoritmo del ejercicio es el siguiente:
# - Obtén todos los ficheros y directorios de un directorio en concreto. Para ello necesitas una función existente
# en la librería os (Sistema Operativo) de Python.
# - Recorre todos los resultados obtenidos por la función anterior. Lo puedes hacer, por ejemplo, con un bucle for.
# - Imprime por pantalla solo aquellos resultados que sean ficheros (para ello también necesitas una función existente en os. \

# Ampliación:
# - Lista los tamaños de los ficheros en formato humano.
# - Recorre de manera recursiva todos los directorios desde tu carpeta personal y muestra los ficheros de cada
# directorio y su tamaño.

import os

contenido = os.listdir('C:/Users/Abraham/Downloads')

for cosa in contenido:
    if os.path.isfile(f'C:/Users/Abraham/Downloads/{cosa}'):
        print(cosa, os.path.getsize(f'C:/Users/Abraham/Downloads/{cosa}'), 'bytes')
