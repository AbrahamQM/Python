# Ejercicio 2
#
#
# Enunciado: Crea una agenda de teléfonos que se gestione por consola, que te permita:
#
#
# 1) Añadir a cualquier persona, indicando nombre y después teléfono
# 2) Buscar el teléfono de una persona
# Objetivo:
# - Aprender a manejar la entrada y la salida por consola.
# - El uso de colecciones (array o diccionario)
#
# Ampliación:
#
#
# - Al buscar a una persona, que te muestre todas aquellas que comiencen por el texto que has introducido. Ejemplo:
#    Introduce un nombre: Pep
#    Resultados:
#    - Pepe 659331013
#    - Pepe Martín 633743551

listado = {}


def añadir():
    print("Indique el nombre:")
    nombre = input()
    print("Indique el teléfono:")
    tel = input()
    listado[nombre] = tel

def registrar():
    mas = 's'
    while mas == 's':
        print("Desea registrar una entrada en el listín (s/n)")
        mas = input()
        if mas == 's':
            añadir()



def buscar():
    print("Indique el nombre:")
    nombre = input()
    if nombre in listado:
        print(f"{nombre}, teléfono: {listado[nombre]}")
    else:
        print("No se encuentra ese registro")


def buscar2():
    print("Indique parte del nombre:")
    nombre = input()
    print("Coincidencias :")
    for persona in listado:
        if nombre in persona:
            print(f'---{persona}, teléfono: {listado[persona]}')


def menu():
    respuesta = ''
    while respuesta != '0':
        print("\n**** Menú ****")
        print("1: añadir registro/s")
        print("2: buscar un registro (nombre completo)")
        print("3: buscar registros (coincidencias)")
        print("0: Salir")

        respuesta = input()

        if respuesta == '1':
            registrar()
        elif respuesta == '2':
            buscar()
        elif respuesta == '3':
            buscar2()


print("Bienvenido al listín telefónico.")

menu()
