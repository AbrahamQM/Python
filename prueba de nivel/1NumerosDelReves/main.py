#Reto 1: Números del revés
import sys

validos = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6} # entiendo que estos son los números  que se pueden girar (suponemos que el 1 es así |)


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
    print("\n** Bienvenido al programa números del revés.")
    valor1 = int(sys.argv[1])
    valor2 = int(sys.argv[2])
    contador = 0
    # comprobamos que los parámetros cumplen valor1 < valor2
    if valor1 <= valor2: 
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
                        print(valor_actual,"->", girado)

        print("El total de números válidos del revés es:", contador)
    else:
        print("ERROR, el rango no es válido!!")


if __name__ == '__main__':
    main()
