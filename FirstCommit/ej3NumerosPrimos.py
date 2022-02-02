# Ejercicio 3
#
# Enunciado: Crea una función que calcule los números primos entre 1 y N, siendo N el parámetro que recibe la función.
#
# Objetivo:
#
# - Uso de bucles anidados
# - El uso de colecciones

def nPrimos(numero):
    num = 1

    print(f"numeros primos entre 1 y {numero}")
    primos = []

    while num <= numero:
        i = 1
        x = 0
        while i <= num:
            if num % i == 0:
                x += 1
            i += 1
        if x == 2:
            primos.append(num)

        num += 1
    return primos

print("Introduzca un nº:")
num = input()
print(nPrimos(int(num)))
