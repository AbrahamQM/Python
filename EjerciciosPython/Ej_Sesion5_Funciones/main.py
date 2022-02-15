# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y
# otra función que calcule el área de un círculo recibiendo el radio del mismo.
import math


def triangulo():
    print("\n--Función para obtener el área de un triángulo--")
    altura = input("Introduzca la altura del triángulo:\n")

    while not altura.isdigit():
        print("Altura incorrecta, ¡¡Por favor introduzca un número!!")
        altura = input("--Introduzca la altura del triángulo:\n")

    base = input("Introduzca la base del triángulo:\n")
    while not base.isdigit():
        print("Base incorrecta, ¡¡Por favor introduzca un número!!")
        base = input("--Introduzca la base del triángulo:\n")

    print("***El triángulo tiene un área de:", (int(base) * int(altura))/2)


def circulo():
    print("\n--Función para obtener el área de un círculo--")
    radio = input("Introduzca el radio del círculo:\n")
    while not radio.isdigit():
        print("Radio incorrecto, ¡¡Por favor introduzca un número!!")
        radio = input("--Introduzca el radio del triángulo:\n")
    print("***El círculo tiene un área de:", (math.pi * (int(radio) ** 2)).__round__(3))


def main():
    print("*****Programa que calcula áreas de triángulos o círculos*****")
    opcion = 0
    while opcion != '3':
        print("\n---MENÚ---\n-1: Triángulo.\n-2: Círculo.\n-3: SALIR")
        opcion = input("-Introduzca un número según desee:\n")
        if opcion == '1':
            triangulo()
        elif opcion == '2':
            circulo()
        elif opcion == '3':
            exit()
        else:
            print("***RESPUESTA ERRÓNEA, recuerde introducir un número 1-3!***")


if __name__ == '__main__':
    main()
