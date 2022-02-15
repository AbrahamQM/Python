# En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora:
# sumar, restar, multiplicar y dividir.

# Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que
# mostrarlos por consola.
import operaciones as op


def main():
    print("*** Programa que ejecuta las operaciones básicas ***\n-Sumar\n-Restar\n-Multiplicar\n-Dividir")

    a = input("Introduzca el primer valor:\n")
    while not a.isdigit():
        print("Valor incorrecto, ¡¡Por favor introduzca un número!!")
        a = input("--Introduzca el primer valor:\n")

    b = input("Introduzca el segundo valor:\n")
    while not b.isdigit():
        print("Valor incorrecto, ¡¡Por favor introduzca un número!!")
        b = input("--Introduzca el segundo valor:\n")

    print(f'Resultado de {a} + {b}: {op.suma(int(a), int(b))}')
    print(f'Resultado de {a} - {b}: {op.resta(int(a), int(b))}')
    print(f'Resultado de {a} * {b}: {op.multiplicacion(int(a), int(b))}')
    print(f'Resultado de {a} / {b}: {op.division(int(a), int(b))}')


if __name__ == '__main__':
    main()
