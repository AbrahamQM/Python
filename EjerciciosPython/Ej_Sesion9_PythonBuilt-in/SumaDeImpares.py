# Tienes que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro
# con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
from functools import reduce

numeros = (8, 96, 5, 1, 3, 82, 4, 27, 99, 6, 2, 4, 8, 3, 6)


def impares(x):
    if x % 2 != 0:
        return True


def suma(a, b):
    return a + b


def main():
    resultado = filter(impares, numeros)
    resultado = reduce(suma, resultado)

    print(f'-Lista de números: {numeros}\n\n***El resultado de sumar sus impares es: {resultado}')


if __name__ == '__main__':
    main()
