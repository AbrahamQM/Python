# Crea un script que le pida al usuario una lista de países (separados por comas).
# Estos se deben almacenar en una lista.
# No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países
# ordenados alfabéticamente y separados por comas.

def main():
    mas = True
    paises = set({})
    while mas:
        paises.add(input("Introduzca nombre de país: ").capitalize())
        otro = input("\n-¿Desea añadir otro país? S/N: ").lower()
        if otro != 's':
            mas = False

    paises = sorted(paises)
    print("-Lista de paises ordenados: ", paises)


if __name__ == '__main__':
    main()
