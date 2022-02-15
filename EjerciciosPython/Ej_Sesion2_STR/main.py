# En este ejercicio tendrás que crear un archivo python donde tendrás que crear una variable a la cual asignarás
# una cadena de texto y la imprimirás por consola.
#
# Por otro lado, tendrás que modificar la variable y después imprimirla por consola para ver la modificación de
# la variable.

def main():
    cadena = 'Esta eS lA cAdena de teXtO A impRimiR pOR conSola.'
    print(cadena)
    cadena = cadena.capitalize()
    print(f'-La cadena capitalizada es:\n{cadena}')


if __name__ == '__main__':
    main()


