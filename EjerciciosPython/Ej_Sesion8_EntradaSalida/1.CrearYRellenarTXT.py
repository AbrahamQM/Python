# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro
# del archivo. Para ello, tendréis que acceder dos veces al archivo creado.


def main():
    # OJO, si se ejecuta más de una vez, dará error porque ya está creado(Salvo que antes de ejecutar el programa
    # eliminemos texto.txt):
    file = open('texto.txt', 'x')
    file.close()

    file = open('texto.txt', 'w')
    file.write(input('Introduzca el texto que quiere guardar en el archivo texto.txt:\n'))
    file.close()



if __name__ == '__main__':
    main()
