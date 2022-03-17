import numpy as np

# input_entrada = np.array([             #SIN SOLUCION
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 15, 0, 14]
# ])
input_entrada = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [15, 13, 14, 0]
])


def ultima_fila(num):
    res_esperado = res(input_entrada)
    pos_esperada = buscar(res(input_entrada), num)
    pos_num = buscar(input_entrada, num)
    ultimo_cuadrante = [(len(input_entrada[0]) - 2, len(input_entrada[1]) - 2),
                        (len(input_entrada[0]) - 2, len(input_entrada[1]) - 1),
                        (len(input_entrada[0]) - 1, len(input_entrada[1]) - 2),
                        (len(input_entrada[0]) - 1, len(input_entrada[1]) - 1)]

    if num != int(res_esperado.max()):
        print("hay un número más")
        sig1 = num + 1
        pos_sig1 = buscar(input_entrada, sig1)
        if sig1 != int(res_esperado.max()):
            sig2 = num + 2
            pos_sig2 = buscar(input_entrada, sig2)
            print("hay dos números más")
        else:
            sig2 = 0
    else:
        sig1 = 0

    print("Entrada:\n", input_entrada)

    def mover_fila_a_derecha():
        print("*******Mover_fila_a_derecha()********")
        pos_cero = buscar(input_entrada, 0)
        while pos_cero[1] != 0:
            intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])
            # print(input_entrada)
            pos_cero = buscar(input_entrada, 0)
        print("///Fin mover_fila_a_derecha")
    def mover_fila_a_izquierda():
        print("*******Mover_fila_a_izquierda()********")
        pos_cero = buscar(input_entrada, 0)
        while pos_cero[1] != len(input_entrada[1])-1:
            intercambiar(input_entrada[pos_cero[0]][pos_cero[1] + 1])
            # print(input_entrada)
            pos_cero = buscar(input_entrada, 0)
        print("///Fin mover_fila_a_izquierda")

    def rotar4():
        print("             000000000     ROTAR4")
        pos_cero = buscar(input_entrada, 0)
        intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
        intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1] + 1])  # Mover a derecha
        intercambiar(input_entrada[pos_cero[0]][pos_cero[1] + 1])  # Bajar fila (misma columna)
        intercambiar(input_entrada[pos_cero[0]][pos_cero[1]])  # Vuelve a pos inicial

        print("                                 -----FIn de rotar4------")


    # ROTAMOS LAS DOS ÚLTIMAS FILAS hasta que num, sig1 y sig2(en caso de haberlo) estén en la esquina inferior derecha
    def cuadrar_esquina():
        print("                Dentro de cuadrar_esquina")
        pos_num = buscar(input_entrada, num)
        if sig2 != 0:
            pos_sig1 = buscar(input_entrada, sig1)
            pos_sig2 = buscar(input_entrada, sig2)
            # hasta que num y los 2 siguientes no estén en el último cuadrante:
            while pos_sig2 not in ultimo_cuadrante or pos_sig1 not in ultimo_cuadrante \
                    or pos_num not in ultimo_cuadrante:
                print("                                       Estoy en el while con 2 numeros mas")
                mover_fila_a_derecha()
                pos_cero = buscar(input_entrada, 0)
                intercambiar(input_entrada[pos_cero[0]-1][pos_cero[1]]) # Subir fila (misma columna)
                mover_fila_a_izquierda()
                pos_cero = buscar(input_entrada, 0)
                intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar 0 (misma columna)
                pos_num = buscar(input_entrada, num)
                pos_sig1 = buscar(input_entrada, sig1)
                pos_sig2 = buscar(input_entrada, sig2)

        elif sig1 != 0:
            pos_sig1 = buscar(input_entrada, sig1)
            # hasta que num y el siguiente no estén en el último cuadrante:
            while pos_sig1 not in ultimo_cuadrante or pos_num not in ultimo_cuadrante:
                mover_fila_a_derecha()
                pos_cero = buscar(input_entrada, 0)
                intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
                mover_fila_a_izquierda()
                pos_cero = buscar(input_entrada, 0)
                intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar 0 (misma columna)
                pos_num = buscar(input_entrada, num)
                pos_sig1 = buscar(input_entrada, sig1)
                print("                                       Estoy en el while con 1 numero mas")
        else:
            # hasta que num no esté en el ultimo_cuadrante
            while pos_num not in ultimo_cuadrante:
                mover_fila_a_derecha()
                pos_cero = buscar(input_entrada, 0)
                intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
                mover_fila_a_izquierda()
                pos_cero = buscar(input_entrada, 0)
                intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar 0 (misma columna)
                pos_num = buscar(input_entrada, num)
                print("                                       Estoy en el while sin mas numeros ")

        print("5555555555555555555555    FIN DE cuadrar_esquina, pos_num:", pos_num)


    cuadrar_esquina() # coloco num y los 2 siguientes si los hay en el ultimo cuadrante y los ordeno

    pos_num = buscar(input_entrada, num)
    giros = 0
    print('Siguientes:', sig1, sig2)
    if sig2 != 0:
        pos_sig2 = buscar(input_entrada, sig2)
        pos_sig1 = buscar(input_entrada, sig1)
        print(f'                    ************************ aqui 1  ')
        while (pos_num != ultimo_cuadrante[0] and pos_sig1 != ultimo_cuadrante[3] and pos_sig2 != ultimo_cuadrante[1]) \
                and giros != 5:
            print(f'                                 --Entro en while de aqui 1\n'
                  f'({pos_num != ultimo_cuadrante[2]} and {pos_sig1 != ultimo_cuadrante[3]}) and {giros != 5}')
            pos_cero = buscar(input_entrada, 0)
            intercambiar(input_entrada[pos_cero[0]][pos_cero[1]-1])
            rotar4()
            giros += 1
            pos_num = buscar(input_entrada, num)
            pos_sig1 = buscar(input_entrada, sig1)
            pos_sig2 = buscar(input_entrada, sig2)
            print(f'                                 ++salgo en while de aqui 1\n'
                  f'({pos_num != ultimo_cuadrante[2]} and {pos_sig1 != ultimo_cuadrante[3]}) and {giros != 5}')

    elif sig1 != 0:
        pos_sig1 = buscar(input_entrada, sig1)
        print("                            ************************aqui 2")
        while (pos_num != ultimo_cuadrante[2] and pos_sig1 != ultimo_cuadrante[3]) and giros != 5:
            pos_cero = buscar(input_entrada, 0)
            intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])
            rotar4()
            giros += 1
            pos_num = buscar(input_entrada, num)
            pos_sig1 = buscar(input_entrada, sig1)


    print(giros)
    if giros != 5:
        pos_cero = buscar(input_entrada, 0)
        intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
        pos_num = buscar(input_entrada, num)
        while pos_num != pos_esperada:#         todo por aquí
            mover_fila_a_derecha()
            pos_cero = buscar(input_entrada, 0)
            intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar fila (misma columna)
            mover_fila_a_izquierda()
            pos_cero = buscar(input_entrada, 0)
            intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)

            pos_num = buscar(input_entrada, num)
            input(f'STOP, pos_num:{pos_num}, pos_esperada:{pos_esperada}')
        pos_cero = buscar(input_entrada, 0)
        intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar fila (misma columna)





# Método que devuelve posiciones 'x' e 'y' del valor numero
def buscar(entrada, numero):
    for x in range(len(entrada)):
        for y in range(len(input_entrada)):
            if entrada[x][y] == numero:
                return x, y


# Método que devuelve un array bidimensional del resultado final esperado
def res(entrada):
    numero = 1
    resultado = np.empty((len(entrada), len(entrada)))  # Creo el array bidimencional sin inicializar
    for x in range(len(entrada)):
        for y in range(len(entrada)):
            if y == len(entrada) - 1 and x == len(entrada) - 1:  # Para el caso del número final
                resultado[x][y] = 0
            else:
                resultado[x][y] = numero
                numero += 1
    return resultado


def intercambiar(numero):
    cero = list(buscar(input_entrada, 0))
    indice = list(buscar(input_entrada, numero))

    input_entrada[cero[0]][cero[1]] = input_entrada[indice[0]][indice[1]]  # Asigno a la posición del 0 el número
    input_entrada[indice[0]][indice[1]] = 0  # Asigno en la posición del número el 0
    print("intercambiar realizado")
    print(input_entrada)


def comprobar_posicion(x, y, num):
    if (x, y) == buscar(input_entrada, num):  # Si num no está en su posición
        return True
    else:
        return False


def mover_cercano(num):
    pos_cero = buscar(input_entrada, 0)
    pos_num = buscar(input_entrada, num)
    print("Mover_cercano Ln:85")
    if abs(pos_num[0] - pos_cero[0]) < abs(pos_num[1] - pos_cero[1]):  # Si se encuentra más cerca del eje x
        print("eje x")
        if pos_num[1] - pos_cero[1] > 0:  # si num está a su derecha del 0
            print(f'if ({pos_num[1]}-{pos_cero[1]}) < 0: (num a la derecha del 0)')
            print(f'pos_cero:{pos_cero}, pos_num:{pos_num}')
            intercambiar(input_entrada[pos_cero[0]][pos_cero[1] + 1])

        elif pos_num[1] - pos_cero[1] < 0:  # si num está a la izquierda del 0
            print(f'elif ({pos_num[1]}-{pos_cero[1]}) > 0: (num a la izquierda del 0)')
            intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])

    else:  # Si se encuentra más cerca del eje y o equidistante
        print("eje Y")
        if (pos_num[0] - pos_cero[0]) < 0:  # si num está encima del 0
            print(f'{num} está encima del 0')
            intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])
        elif (pos_num[0] - pos_cero[0]) > 0:  # si num está debajo del 0
            print(f'{num} está debajo del 0 pos_cero:{pos_cero} pos_num:{pos_num}')
            intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])
        else:
            print("No entró a intercambiar pos_cero, pos_num:", pos_cero[0], pos_num)


def resuelto():  # Comprueba que el puzzle está resuelto (True) o no (False)
    esperado = res(input_entrada)
    for x in range(len(input_entrada)):
        for y in range(len(input_entrada)):
            if input_entrada[x][y] != esperado[x][y]:
                return False
    return True


def girar3_reloj(num):  # Método que hace girar en sentido de las agujas de reloj 3 posiciones
    print("GIRAR3 num: ", num)
    pos_cero = buscar(input_entrada, 0)
    print(input_entrada, "\n")
    intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])
    print(input_entrada, "\n")
    intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1] - 1])
    print(input_entrada, "\n")
    intercambiar(num)


def girar3_reloj_inv(num):  # Método que hace girar en sentido CONTRARIO a las agujas de reloj 3 posiciones
    print("GIRAR3 num: ", num)
    pos_cero = buscar(input_entrada, 0)
    print(input_entrada, "\n")
    intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])
    print(input_entrada, "\n")
    intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1] - 1])
    print(input_entrada, "\n")
    intercambiar(num)


#  Método que mueve el 0 por debajo del número si el num está en la esquina superior izquierda del 0
def rodearXdebajo_a_izquierda():
    pos_cero = buscar(input_entrada, 0)
    print("**rodearXdebajo_a_izquierda():** Ln:132")
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1] - 1])
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1] - 2])
    intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 2])


def rodearXdebajo_a_derecha():
    pos_cero = buscar(input_entrada, 0)
    print("**rodearXdebajo_a_derecha():** Ln:153")
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1] + 1])
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1] + 2])
    intercambiar(input_entrada[pos_cero[0]][pos_cero[1] + 2])


# Método para resolver cuando num está en el extremo derecho del array debajo de su posición esperada
def cambiar_esquina():
    print("--------Cambiar esquina")
    pos_cero = buscar(input_entrada, 0)
    while pos_cero[1] > 0:
        intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])
        pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])
    pos_cero = buscar(input_entrada, 0)
    while pos_cero[1] < len(input_entrada[0]) - 1:
        intercambiar(input_entrada[pos_cero[0]][pos_cero[1] + 1])
        pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1] - 1])
    intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])
    # intercambiar(input_entrada[pos_cero[0]][pos_cero[1]])
    pos_cero = buscar(input_entrada, 0)
    while pos_cero[1] > 0:
        intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])
        pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])
    print("///FIN DE CAMBIAR_ESQUINA////")


ultima_fila(13)
