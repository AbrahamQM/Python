#Reto 1: Números del revés
# Descripción del reto
# Un número del revés es un número entero que aparece igual cuando se gira 180 grados,
# por ejemplo:
# 1961 → 1961 ✅
# 88 → 88 ✅
# 66 → 99 ❌
# 101 → 101 ✅
# Debes crear una función capaz de sacar los números de un rango que sean reversibles.
# Input:
# La función recibirá dos valores. Estos dos valores representarán los límites superior e
# inferior de un rango.
# Output:
# La función debe devolver los números y la cantidad total de números invertidos válidos
# dentro del rango de los dos argumentos de entrada, incluidos los límites superior e inferior.
# Detalles importantes de la prueba
# ● El primer argumento siempre será menor que el segundo argumento (es decir, el
# rango siempre deberá ser válido).

validos = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}


# Método que recibe como parámetro una lista de enteros y devuelve un entero con los números girados 180º
def girar(listado):
    for x in range(len(listado)):  # Sustituyo cada valor por el número invertido
        listado[x] = validos[listado[x]]

    listado.reverse()  # Invierto el orden

    resultado = ''
    for num in listado: # Concateno la lista de dígitos
        resultado += str(num)

    return int(resultado)


def main():
    print("\n** Bienvenido al programa números del revés. **\n\n-Introducir dos valores el 1º menor que el 2º:")
    valor1 = int(input('\nIntroduzca el primer valor:\n'))
    valor2 = int(input('\nIntroduzca el segundo valor:\n'))
    contador = 0
    for valor_actual in range(valor1, valor2 + 1):
        lista = [int(a) for a in str(valor_actual)]
        resultado = ''
        for digito in lista:
            if digito not in validos:
                break  # Descarto los números que contengan dígitos no válidos para girar
            resultado += str(digito)  # Concateno a resultado los dígitos que si se pueden girar

        if resultado != '':  # Compruebo que se han añadido dígitos a resultado
            if int(resultado) == valor_actual:  # Compruebo que el resultado contiene el nº completo(no hubo descartados)
                girado = girar(lista)
                if valor_actual == girado:  # Si son iguales incremento contador y los imprimo
                    contador += 1
                    print(valor_actual, girado)

    print("El total de números válidos del revés es:", contador)


if __name__ == '__main__':
    main()

