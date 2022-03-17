# Descripción del reto
# Un rompecabezas deslizante es un rompecabezas combinado que desafía al jugador a
# deslizar piezas (con frecuencia planas) a lo largo de ciertas rutas (generalmente en un
# tablero) para establecer una configuración final determinada.
# Su objetivo para este reto es escribir una función que produzca una secuencia de
# movimientos de fichas que resuelva el rompecabezas.


# Input del algoritmo
# Una matriz/lista n x n compuesta por valores enteros que van de 0 a n^2 - 1 (inclusive), que
# representa una cuadrícula cuadrada.
# Ten en cuenta que siempre habrá una ficha vacía (representada por 0) para permitir el
# movimiento de fichas adyacentes.
# Output del algoritmo
# Una matriz/lista compuesta por cualquiera (pero no necesariamente todos) de los números
# enteros de 1 a n^2 - 1, inclusive.
# Esto representa la secuencia de movimientos de fichas para una transición exitosa del
# estado inicial sin resolver al estado resuelto. Si el rompecabezas no se puede resolver,
# devolverá None (Python).

# Detalles importantes para la prueba
# ● El input debe ser válido.
# ● El rango de valores para n es: 10 >= n >= 3
import numpy as np
#  Otras pruebas mas complicadas todo no tiene solucion
# input_entrada = np.array([
#     [7, 1, 3, 4],
#     [5, 2, 6, 8],
#     [9, 10, 0, 11],
#     [13, 14, 15, 12]
# ])

# todo input entrada de ejemplo en la prueba
# input_entrada = np.array([
#     [1, 2, 3, 4],
#     [5, 0, 6, 8],
#     [9, 10, 7, 11],
#     [13, 14, 15, 12]
# ])

input_entrada = np.array([
    [0, 3, 4],
    [1, 2, 5],
    [8, 7, 6],
])

contador_stop = 0

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


def girar3_reloj_inv(num): # Método que hace girar en sentido CONTRARIO a las agujas de reloj 3 posiciones
    print("GIRAR3 num: ", num)
    pos_cero = buscar(input_entrada, 0)
    print(input_entrada, "\n")
    intercambiar(input_entrada[pos_cero[0]-1][pos_cero[1]])
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
        intercambiar(input_entrada[pos_cero[0]][pos_cero[1]-1])
        pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada[pos_cero[0]-1][pos_cero[1]])
    pos_cero = buscar(input_entrada, 0)
    while pos_cero[1] < len(input_entrada[0])-1:
        intercambiar(input_entrada[pos_cero[0]][pos_cero[1]+1])
        pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada[pos_cero[0]+1][pos_cero[1]])
    intercambiar(input_entrada[pos_cero[0]+1][pos_cero[1]-1])
    intercambiar(input_entrada[pos_cero[0]][pos_cero[1]-1])
    # intercambiar(input_entrada[pos_cero[0]][pos_cero[1]])
    pos_cero = buscar(input_entrada, 0)
    while pos_cero[1] > 0:
        intercambiar(input_entrada[pos_cero[0]][pos_cero[1]-1])
        pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada[pos_cero[0]+1][pos_cero[1]])
    print("///FIN DE CAMBIAR_ESQUINA////")


# todo ojo aqui pongo el código de ultima fila, borrar si no funciona
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




def mover():
    num = 1  # Num actual a colocar se va incrementando

    while not resuelto():
        pos_cero = buscar(input_entrada, 0)
        pos_esperada = buscar(res(input_entrada), num)
        pos_num = buscar(input_entrada, num)
        print(f'pos_num:{pos_num}, pos_esperada:{pos_esperada}, pos_cero:{pos_cero}\n{input_entrada} LN:193')

        # Si num no está en su posición pero si en su fila
        if not comprobar_posicion(pos_esperada[0], pos_esperada[1], num) and num in input_entrada[pos_esperada[0]]:
            print(f'El numero {num}, no esta en su posición, pero SI en su fila LN:197')

            # Si num es colindante al 0 y el 0 está en la misma fila que num
            if (pos_num == (pos_esperada[0], pos_esperada[1] + 1) or pos_num == (
                    pos_esperada[0] + 1, pos_esperada[1]) or pos_num == (pos_esperada[0] - 1, pos_esperada[1]) or
                pos_num == (pos_esperada[0], pos_esperada[1] - 1)) and pos_cero[0] == pos_num[0]:

                # Si el cero está a la izda de num y hay que mover num a izda
                if pos_cero[1] < pos_num[1] and pos_esperada[1] < pos_num[1]:

                    print(f'{num} es colindante al 0 y el 0 está en la misma fila que {num}\n'
                          f'El cero está a la izda de num y hay que mover num a izda LN:208')
                    intercambiar(num)
                    continue
                # Si el 0 está a la derecha de num y hay que mover a la izda y no estamos en la última fila
                elif pos_cero[1] > pos_num[1] > pos_esperada[1] and pos_cero[0] < len(input_entrada[1])-1:
                    print("num está es colindante al 0, están en la misma fila, Hay que mover num a la izda"
                          " y el 0 está a su derecha LN:214")
                    rodearXdebajo_a_izquierda()
                    continue
            #  num no es colindante a 0 y el numero está es la esquina superior-izda del 0
            if pos_cero[0] - 1 == pos_num[0] and pos_cero[1] - 1 == pos_num[1]:
                intercambiar(input_entrada[pos_cero[0]][pos_num[1]]) # movemos el 0 a su izquierda 1 posición
                intercambiar(input_entrada[pos_cero[0]][pos_num[1]-1]) # movemos el 0 a su izquierda 2 posición
                intercambiar(input_entrada[pos_cero[0]-1][pos_num[1]-1]) # movemos el 0 arriba (queda a la izda de num)
                continue

            # Si num está en la misma fila que el 0 pero no es colindante y pos_esperada no está en la última fila
            elif pos_cero[0] == pos_num[0] and pos_esperada[0] < len(input_entrada[1]) - 1:
                print(
                    f'El numero {num}, no esta en su posición, pero SI en su fila, NO ES COLINDANTE a 0 pero SI estan '
                    f'en la misma fila LN:227')
                print(f' mover_cercano({num})')
                mover_cercano(num)
                continue

            # Si num es colindante al cero,
            elif (pos_cero == (pos_num[0], pos_num[1] + 1) or pos_cero == (pos_num[0] + 1, pos_num[1])
                  or pos_cero == (pos_num[0] - 1, pos_num[1])
                  or pos_cero == (pos_num[0], pos_num[1] - 1)):
                print(f'{num} es colindante al 0,  LN:236')

                if pos_num[0] == 0 and pos_num[1] != 0:  # Si el número está en la fila superior pero no en columna 0
                    girar3_reloj(num)
                    continue

                elif pos_esperada[0] == len(input_entrada[1]) - 1: # si pos_esperada está en la última fila
            #                             todo vamos por aqui con el último numero
                    ultima_fila(num)

            # # Si el num no colindante a 0, 0 está en(fila inferior, columna derecha),
            # # Y num está a la derecha de pos_esperada y en su fila todo revisar esto tambien falta poner condición
            # elif ():
            #     rodearXdebajo_a_izquierda()
            #     continue

            else:  # Si num no es colindante a 0, ni están en la misma fila
                print("ELSE LN:249")
                print(f'{num}, no esta en su posición, pero SI en su fila, NO ES COLINDANTE a 0, 0 y {num} no están en '
                      f'la misma fila')
                mover_cercano(num)
                continue


        # Si num no está en su posición ni en su fila
        elif not comprobar_posicion(pos_esperada[0], pos_esperada[1], num) and num not in input_entrada[
            pos_esperada[0]]:
            print(f'El numero {num}, no esta en su posición, NI en su fila LN:259 {len(input_entrada[1])}')

            # Si es colindante al 0 y el num no está en la columna esperada y el cero está a la izq de num
            if (pos_cero == (pos_num[0], pos_num[1] + 1) or pos_cero == (pos_num[0] + 1, pos_num[1])
                    or pos_cero == (pos_num[0] - 1, pos_num[1]) or pos_cero == (pos_num[0], pos_num[1] - 1)) \
                    and pos_num[1] != pos_esperada[1] and pos_num[1] > pos_cero[1]:
                print(f'***Intercambiar*** {num} es colindante al 0 pero el 0 no está en la misma columna que {num} LN:266')
                if pos_cero[1] == 0: # El 0 está en la primera columna
                    print("***OJO ahora aqui el 0 está en la primera columna LN:268")
                    rodearXdebajo_a_derecha()
                    continue

                else:
                    intercambiar(num)
                    continue

            # 0 esta a la derecha de num, numero esta debajo de pos_esperada, num está en la columna esperada,
            # la columna esperada no es la última
            elif pos_cero == (pos_num[0], pos_num[1] + 1) and pos_num[0] > pos_esperada[0] and \
                    pos_num[1] == pos_esperada[1] and pos_esperada[1] < len(input_entrada[1] - 1):
                print(f'El numero {num}, no esta en su posición,SI DEBAJO de su fila,Si en su columna, '
                      f'y si a la derecha del 0 **LN:275, ')
                girar3_reloj_inv(num)
                continue

            # 0 está sobre el num y pos_esperada es la del 0
            elif pos_cero == (pos_num[0] - 1, pos_num[1]) and pos_esperada == pos_cero:
                print("0 está sobre el num y pos_esperada es la del 0, Ln:280")
                intercambiar(num)
                continue


            # Pero Si es colindante al 0, num esta en la columna esperada, la columna no es la última y el 0 no
            # está encima del num
            elif ((pos_cero == (pos_num[0], pos_num[1] + 1) or pos_cero == (pos_num[0] + 1, pos_num[1])
                    or pos_cero == (pos_num[0] - 1, pos_num[1]) or pos_cero == (pos_num[0], pos_num[1] - 1))) \
                    and pos_num[0] > pos_esperada[0] and pos_num[1] == pos_esperada[1] \
                    and pos_esperada[1] < len(input_entrada[1]) - 1 and pos_cero[0] <= pos_num[0]:
                print(f'El numero {num}, no esta en su posición,SI DEBAJO de su fila,Si en su columna LN:298, '
                      f'y si colindante al 0 pos_esperada[1]:{pos_esperada[1]} < len(input_entrada[1]-1:'
                      f'{len(input_entrada[1]) - 1}')
                rodearXdebajo_a_derecha()
                intercambiar(input_entrada[pos_cero[0]-1][pos_cero[1]+2])
                intercambiar(input_entrada[pos_cero[0]-1][pos_cero[1]+1])
                continue

            # Pero Si es colindante al 0, num esta en la columna esperada, la columna SI es la última y el 0 no
            # está encima del num
            elif ((pos_cero == (pos_num[0], pos_num[1] + 1) or pos_cero == (pos_num[0] + 1, pos_num[1])
                   or pos_cero == (pos_num[0] - 1, pos_num[1]) or pos_cero == (pos_num[0], pos_num[1] - 1))) \
                 and pos_num[0] > pos_esperada[0] and pos_num[1] == pos_esperada[1] \
                 and pos_esperada[1] == len(input_entrada[1]) - 1 and pos_cero[0] <= pos_num[0]:
                print(f'El numero {num}, no esta en su posición,SI DEBAJO de su fila,Si en su columna LN:312, '
                      f'y si colindante al 0 pos_esperada[1]:{pos_esperada[1]} < len(input_entrada[1]-1:'
                      f'{len(input_entrada[1]) - 1}')
                # Si num no está en esquina inferior derecha
                if pos_num != (len(input_entrada[0])-1, len(input_entrada[1])-1):
                    cambiar_esquina()
                    continue
                # Si está en esq inferior derecha y su posición esperada es justo encima de donde está
                elif pos_esperada == (pos_num[0]-1, pos_num[1]):
                    cambiar_esquina()
                    continue

            # Si el num esta a la izda de su posición, el 0 a la izda del num
            elif pos_num[1]<pos_esperada[1] and pos_cero[1]<pos_num[1]:
                print("elif en lin 323")
                rodearXdebajo_a_derecha()
                continue

            # Si el número está en la esq inferior derecha
            elif pos_num == (len(input_entrada[0])-1, len(input_entrada[1])-1):
                print(f'{num} en esq inferior derecha')
                input("Stop en elif")
                # muevo el cero mientras el 0 no esté encima de num
                while pos_cero != (len(input_entrada[0]) - 2, len(input_entrada[1]) - 1):
                    mover_cercano(input_entrada[len(input_entrada[0]) - 2][len(input_entrada[1]) - 1])
                    pos_cero = buscar(input_entrada, 0)
                intercambiar(num) # el 0 queda en esq inferior derecha
                # Muevo el 0 hasta la izquierda de num
                intercambiar(input_entrada[len(input_entrada[0]) - 1][len(input_entrada[1]) - 2])
                intercambiar(input_entrada[len(input_entrada[0]) - 2][len(input_entrada[1]) - 2])
                continue


            else:
                print("Else en lin:319")
                # intercambiar(input_entrada[pos_cero[0]+1][pos_cero[1]])
                mover_cercano(num)
                continue

        # num en su posición
        else:
            print(f'Estamos en el else general El {num} está en su pocicion')
            num += 1
            print(f'****************Ahora num es: {num} *********************')

        print(input_entrada)
        global contador_stop
        contador_stop += 1
        input(f'Stop : {contador_stop}')

    print("!!! FELICIDADES, EL ROMPECABEZAS ESTÁ RESUELTO !!!")

def main():
    print("# Transiciones a realizar para resolver el rompecabezas:\n")
    # print("El array de entrada es:\n", input_entrada)
    mover()


if __name__ == '__main__':
    main()
