# Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
def main():
    edad = input("--Introduzca su edad:\n")
    while not edad.isdigit():
        print("Edad incorrecta, ¡¡Por favor introduzca un número!!")
        edad = input("--Introduzca su edad:\n")
    if int(edad) > 17:
        print("-Es mayor de edad")
    else:
        print("-No es mayor de edad")


if __name__ == '__main__':
    main()

