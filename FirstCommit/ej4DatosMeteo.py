# Ejercicio 4
#
# Enunciado: Utilizando la API de https://openweathermap.org/ y realizando una petición a
# https://api.openweathermap.org/data/2.5/weather?q={city%20name}&appid={API%20key} ,
# obtén la temperatura máxima y mínima, para la ciudad que proporcione el usuario.
#
#
# Objetivo:
#
# Aprender a utilizar librerías externas (en este caso, requests)
#
# Manipular el resultado de la petición (JSON)

import requests
import json

key = 'd9b3ef90577476eb8ae5c82770c8f20f'


def conv(grados):
    return round(grados - 273.15)


def obtener():
    print("Introduzca nombre de ciudad para obtener los datos meteorológicos:")

    city = input()
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}')
    if r.status_code == 200:
        respJson = json.loads(r.text)

        tiempo = respJson['main']  # tiempo es un diccionario
        print(f'-Ciudad: {city}, Coordenadas: {respJson["coord"]}')
        print(f'-Temperatura actual: {conv(tiempo["temp"])}ºCentígrados')
        print(f'-Temperatura Mínima: {conv(tiempo["temp_min"])}ºC \n-Temperatura Máxima: {conv(tiempo["temp_max"])}ºC')
    else:
        print(f'No se reconoce la ciudad "{city}". Revise el nombre y vuelva a intentarlo...')

print("****Bienvenido a Datos Meteorológicos (Implementado por Abraham Quintana)****")
obtenerMas = True


def mas():
    print("\n------------------------------------------------------------")
    print("|  --Si desea obtener los datos de otra ciudad Pulse Enter:  |")
    print("|  --En caso contrario pulse (n + Enter):                    |")
    print("------------------------------------------------------------")
    resp = input()
    if resp == 'n':
        global obtenerMas
        obtenerMas = False


while obtenerMas:
    obtener()
    mas()
