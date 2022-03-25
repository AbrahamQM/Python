# Rompecabezas deslizante

# Admite paso por parámetro del array o usar uno con el nombre input_entrada
# Soy consciente de que necesita refactorización ya que habrá código redundante,
# pero lo entrego hasta el punto al que llegué dentro del plazo permitido. Funciona.
import math

import numpy as np
import sys
import ultimaFila as u

#  Otras pruebas mas complicadas no tiene solucion todo el código falla, revisar
input_entrada = np.array([
    [7, 1, 3, 4],
    [5, 2, 6, 8],
    [9, 10, 0, 11],
    [13, 14, 15, 12]
])

# todo input entrada de ejemplo en la prueba
# input_entrada = np.array([
#    [1, 2, 3, 4],
#    [5, 0, 6, 8],
#    [9, 10, 7, 11],
#    [13, 14, 15, 12]
# ])
#
# input_entrada = np.array([  # Sin solucion
#     [0, 3, 4],
#     [1, 2, 5],
#     [8, 7, 6],
# ])
# input_entrada = np.array([  # Con solucion
#     [0, 3, 4],
#     [1, 6, 8],
#     [2, 7, 5],
# ])

# input_entrada = np.array([
#     [7, 1, 3, 4, 16],
#     [5, 2, 6, 8, 17],
#     [9, 10, 0, 11, 18],
#     [13, 14, 15, 12, 19],
#     [21, 22, 20, 23, 24]
# ])

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
    
    print("    |\n    V\n", input_entrada)


def comprobar_posicion(x, y, num):
    if (x, y) == buscar(input_entrada, num):  # Si num no está en su posición
        return True
    else:
        return False


def mover_cercano(num):
    pos_cero = buscar(input_entrada, 0)
    pos_num = buscar(input_entrada, num)
    # print("Mover_cercano Ln:85")
    if abs(pos_num[0] - pos_cero[0]) < abs(pos_num[1] - pos_cero[1]):  # Si se encuentra más cerca del eje x
        # print("eje x")
        if pos_num[1] - pos_cero[1] > 0:  # si num está a su derecha del 0
            # print(f'if ({pos_num[1]}-{pos_cero[1]}) < 0: (num a la derecha del 0)')
            # print(f'pos_cero:{pos_cero}, pos_num:{pos_num}')
            intercambiar(input_entrada[pos_cero[0]][pos_cero[1] + 1])

        elif pos_num[1] - pos_cero[1] < 0:  # si num está a la izquierda del 0
            # print(f'elif ({pos_num[1]}-{pos_cero[1]}) > 0: (num a la izquierda del 0)')
            intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])

    else:  # Si se encuentra más cerca del eje y o equidistante
        # print("eje Y")
        if (pos_num[0] - pos_cero[0]) < 0:  # si num está encima del 0
            # print(f'{num} está encima del 0')
            intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])
        elif (pos_num[0] - pos_cero[0]) > 0:  # si num está debajo del 0
            # print(f'{num} está debajo del 0 pos_cero:{pos_cero} pos_num:{pos_num}')
            intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])
        # else:
        #     print("No entró a intercambiar pos_cero, pos_num:", pos_cero[0], pos_num)


def resuelto():  # Comprueba que el puzzle está resuelto (True) o no (False)
    esperado = res(input_entrada)
    for x in range(len(input_entrada)):
        for y in range(len(input_entrada)):
            if input_entrada[x][y] != esperado[x][y]:
                return False
    return True


def girar3_reloj(num):  # Método que hace girar en sentido de las agujas de reloj 3 posiciones
    # print("GIRAR3 num: ", num)
    pos_cero = buscar(input_entrada, 0)
    # print(input_entrada, "\n")
    intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])
    # print(input_entrada, "\n")
    intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1] - 1])
    # print(input_entrada, "\n")
    intercambiar(num)


def girar3_reloj_inv(num):  # Método que hace girar en sentido CONTRARIO a las agujas de reloj 3 posiciones
    # print("GIRAR3 num: ", num)
    pos_cero = buscar(input_entrada, 0)
    # print(input_entrada, "\n")
    intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])
    # print(input_entrada, "\n")
    intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1] - 1])
    # print(input_entrada, "\n")
    intercambiar(num)


#  Método que mueve el 0 por debajo del número
def rodearXdebajo_a_izquierda():
    pos_cero = buscar(input_entrada, 0)
    # print("**rodearXdebajo_a_izquierda():** Ln:132")
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1] - 1])
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1] - 2])
    intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 2])


def rodearXdebajo_a_derecha():
    pos_cero = buscar(input_entrada, 0)
    # print("**rodearXdebajo_a_derecha():** Ln:153")
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1] + 1])
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1] + 2])
    intercambiar(input_entrada[pos_cero[0]][pos_cero[1] + 2])


# Método para resolver cuando num está en el extremo derecho del array debajo de su posición esperada
def cambiar_esquina():
    # print("--------Cambiar esquina")
    pos_cero = buscar(input_entrada, 0)
    while pos_cero[1] > 0:  # muevo 0 a izda
        intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])
        pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subo
    pos_cero = buscar(input_entrada, 0)
    while pos_cero[1] < len(input_entrada[0]) - 1: # Muevo 0 a derecha
        intercambiar(input_entrada[pos_cero[0]][pos_cero[1] + 1])
        pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1] - 1])
    intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])
    pos_cero = buscar(input_entrada, 0)
    while pos_cero[1] > 0:
        intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])
        pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])



def mover():
    num = 1  # Num actual a colocar se va incrementando
    ultima = 0
    while not resuelto():
        pos_cero = buscar(input_entrada, 0)
        pos_esperada = buscar(res(input_entrada), num)
        pos_num = buscar(input_entrada, num)
        # print(f'pos_num:{pos_num}, pos_esperada:{pos_esperada}, pos_cero:{pos_cero}\n{input_entrada} LN:193')

        # Si num no está en su posición pero si en su fila
        if not comprobar_posicion(pos_esperada[0], pos_esperada[1], num) and num in input_entrada[pos_esperada[0]]:
            # print(f'El numero {num}, no esta en su posición, pero SI en su fila LN:197')
            if ultima == None:
                print("ultima es:", ultima)
                return ultima
            # Si num es colindante al 0 y el 0 está en la misma fila que num
            if (pos_num == (pos_esperada[0], pos_esperada[1] + 1) or pos_num == (
                    pos_esperada[0] + 1, pos_esperada[1]) or pos_num == (pos_esperada[0] - 1, pos_esperada[1]) or
                pos_num == (pos_esperada[0], pos_esperada[1] - 1)) and pos_cero[0] == pos_num[0]:

                # Si el cero está a la izda de num y hay que mover num a izda
                if pos_cero[1] < pos_num[1] and pos_esperada[1] < pos_num[1]:
                    # print(f'{num} es colindante al 0 y el 0 está en la misma fila que {num}\n'
                    #       f'El cero está a la izda de num y hay que mover num a izda LN:208')
                    print("ln: 361")
                    intercambiar(num)
                    continue

                # Si el 0 está a la derecha de num y hay que mover a la izda y no estamos en la última fila
                elif pos_cero[1] > pos_num[1] > pos_esperada[1] and pos_cero[0] < len(input_entrada[1]) - 1:
                    # print("num está es colindante al 0, están en la misma fila, Hay que mover num a la izda"
                    #       " y el 0 está a su derecha LN:214")
                    print("ln: 368")
                    rodearXdebajo_a_izquierda()
                    continue
            #  num no es colindante a 0 y el numero está es la esquina superior-izda del 0
            if pos_cero[0] - 1 == pos_num[0] and pos_cero[1] - 1 == pos_num[1]:
                print("LN: 372")
                intercambiar(input_entrada[pos_cero[0]][pos_num[1]])  # movemos el 0 a su izquierda 1 posición
                intercambiar(input_entrada[pos_cero[0]][pos_num[1] - 1])  # movemos el 0 a su izquierda 2 posición
                intercambiar(input_entrada[pos_cero[0] - 1][pos_num[1] - 1])  # movemos el 0 arriba
                continue

            # Si num está en la misma fila que el 0 pero no es colindante y pos_esperada no está en la última fila
            elif pos_cero[0] == pos_num[0] and pos_cero[1] != pos_num[1]-1 and pos_cero[1] != pos_num[1]+1 \
                    and pos_esperada[0] < len(input_entrada[1]) - 1:
                # print(
                # f'El numero {num}, no esta en su posición, pero SI en su fila, NO ES COLINDANTE a 0 pero SI estan '
                # f'en la misma fila LN:227')
                print("LN: 384")
                mover_cercano(num)
                continue

            # Si num es colindante al cero,
            elif (pos_cero == (pos_num[0], pos_num[1] + 1) or pos_cero == (pos_num[0] + 1, pos_num[1])
                  or pos_cero == (pos_num[0] - 1, pos_num[1])
                  or pos_cero == (pos_num[0], pos_num[1] - 1)):
                print("LN:395")

                if pos_num[0] == 0 and pos_num[1] != 0:  # Si el número está en la fila superior pero no en columna 0
                    print("ln: 398")
                    girar3_reloj(num)
                    continue

                # Si num está JUSTO a la derecha del 0 y pos_esperada está a la izquierda
                elif pos_num == (pos_cero[0], pos_cero[1]+1) and pos_esperada[1] < pos_num[1]:
                    print("LN:404")
                    intercambiar(num)

                # Si num está JUSTO a la izquierda del 0 y pos_esperada está a la izquierda de num y no es última fila
                elif pos_num == (pos_cero[0], pos_cero[1]-1) and pos_esperada[1] < pos_num[1] \
                    and pos_num[0] < len(input_entrada[1])-1:
                    print("LN:256")
                    rodearXdebajo_a_izquierda()
                    continue

                elif pos_esperada[0] == len(input_entrada[1]) - 1 and ultima != None:  # si pos_esperada está en la última fila
                    if len(input_entrada[0]) > 3:
                        print("ln: 262. ultima=", ultima)
                        ultima = u.ultima_fila(num)

                    else:
                        return None
                    #     print("\n         ULTIMA FILA <= 3X3:")
                    #     ultima_fila(num)

                # Si el número está JUSTO encima del 0 y no es la primera columna
                elif pos_num == (pos_cero[0]-1, pos_cero[1]) and pos_num[1] != 0:  # Lo rodeo hasta su izda
                    print("--LN:425")
                    intercambiar(input_entrada[pos_cero[0]][pos_cero[1]-1])
                    intercambiar(input_entrada[pos_cero[0]-1][pos_cero[1]-1])
                    input("¿Deberia entrar aqui?")

            else:  # Si num no es colindante a 0, ni están en la misma fila
                #       f'la misma fila')
                print("LN:278")
                mover_cercano(num)
                continue


        # Si num no está en su posición ni en su fila
        elif not comprobar_posicion(pos_esperada[0], pos_esperada[1], num) and num not in input_entrada[
            pos_esperada[0]]:
            # print(f'El numero {num}, no esta en su posición, NI en su fila LN:259 {len(input_entrada[1])}')
            print("LN:418")
            # Si es colindante al 0 y el num no está en la columna esperada y el cero está a la izq de num
            if (pos_cero == (pos_num[0], pos_num[1] + 1) or pos_cero == (pos_num[0] + 1, pos_num[1])
                or pos_cero == (pos_num[0] - 1, pos_num[1]) or pos_cero == (pos_num[0], pos_num[1] - 1)) \
                    and pos_num[1] != pos_esperada[1] and pos_num[1] > pos_cero[1]:
                print("If en Ln:421")

                # El 0 está justo a la izda de num y la columna esperada a la derecha de num y no es última fila
                if pos_cero == (pos_num[0], pos_num[1] - 1) and pos_esperada[1] > pos_num[1] \
                        and pos_num[0] != len(input_entrada[1])-1:
                    # print("***OJO ahora aqui el 0 está en la primera columna LN:268")
                    print("LN:427")
                    rodearXdebajo_a_derecha()
                    continue

                # Si el 0 está justo a la izq de num y la columna esperada está a la derecha de num
                # elif pos_cero == (pos_num[0], pos_num[1]-1) and pos_esperada[1] > pos_num[1]:

                # Si no está en la última fila
                elif pos_num[0] != len(input_entrada[1])-1:
                    print("LN:431")
                    intercambiar(num)
                    continue
                # Si num está en la última fila pero pos_esperada no
                elif pos_esperada[0] != len(input_entrada[1])-1:
                    print("lo subo una fila")
                    intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])
                    intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1] + 1])
                    intercambiar(input_entrada[pos_cero[0]][pos_cero[1] + 1])
                    input()
                    continue


            # 0 esta a la derecha de num, numero esta debajo de pos_esperada, num está en la columna esperada,
            # la columna esperada no es la última
            elif pos_cero == (pos_num[0], pos_num[1] + 1) and pos_num[0] > pos_esperada[0] and \
                    pos_num[1] == pos_esperada[1] and pos_esperada[1] < len(input_entrada[1] - 1):
                # print(f'El numero {num}, no esta en su posición,SI DEBAJO de su fila,Si en su columna, '
                #       f'y si a la derecha del 0 **LN:275, ')
                print("LN:440")
                girar3_reloj_inv(num)
                continue

            # 0 está sobre el num y pos_esperada es la del 0
            elif pos_cero == (pos_num[0] - 1, pos_num[1]) and pos_esperada == pos_cero:
                # print("0 está sobre el num y pos_esperada es la del 0, Ln:280")
                print("LN:446")
                intercambiar(num)
                continue

            # Pero Si es colindante al 0, num esta en la columna esperada, la columna no es la última y el 0 no
            # está encima del num y no está en última fila
            elif ((pos_cero == (pos_num[0], pos_num[1] + 1) or pos_cero == (pos_num[0] + 1, pos_num[1])
                   or pos_cero == (pos_num[0] - 1, pos_num[1]) or pos_cero == (pos_num[0], pos_num[1] - 1))) \
                    and pos_num[0] > pos_esperada[0] and pos_num[1] == pos_esperada[1] \
                    and pos_esperada[1] < len(input_entrada[1]) - 1 and pos_cero[0] <= pos_num[0] \
                    and pos_num[0] != len(input_entrada[0]) - 1:
                # print(f'El numero {num}, no esta en su posición,SI DEBAJO de su fila,Si en su columna LN:298, '
                #       f'y si colindante al 0 pos_esperada[1]:{pos_esperada[1]} < len(input_entrada[1]-1:'
                #       f'{len(input_entrada[1]) - 1}')
                print("LN:465")
                rodearXdebajo_a_derecha()
                intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1] + 2])
                intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1] + 1])
                continue

            # Pero Si es colindante al 0, num esta en la columna esperada, la columna SI es la última y el 0 no
            # está encima del num
            elif ((pos_cero == (pos_num[0], pos_num[1] + 1) or pos_cero == (pos_num[0] + 1, pos_num[1])
                   or pos_cero == (pos_num[0] - 1, pos_num[1]) or pos_cero == (pos_num[0], pos_num[1] - 1))) \
                    and pos_num[0] > pos_esperada[0] and pos_num[1] == pos_esperada[1] \
                    and pos_esperada[1] == len(input_entrada[1]) - 1 and pos_cero[0] <= pos_num[0]:
                print("LN:477")  # todo código redundante if-elif iguales?

                # Si num no está en esquina inferior derecha ni JUSTO debajo de pos_esperada y cero justo a la izda de num
                if pos_num != (len(input_entrada[0]) - 1, len(input_entrada[1]) - 1) \
                        and pos_num != (pos_esperada[0] + 1, pos_esperada[1]) and pos_cero == (
                pos_num[0], pos_num[1] - 1):
                    print("LN:481")
                    intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])
                    intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1] + 1])
                    intercambiar(input_entrada[pos_cero[0]][pos_cero[1] + 1])
                    input("compruebalo")
                    continue

                # Si su posición esperada es justo encima de donde está
                elif pos_esperada == (pos_num[0] - 1, pos_num[1]):
                    print("LN: 478")
                    cambiar_esquina()
                    continue

            # Si el num esta a la izda de su posición, el 0 a la izda del num
            elif pos_num[1] < pos_esperada[1] and pos_cero[1] < pos_num[1]:
                print("elif en lin 483")
                rodearXdebajo_a_derecha()
                continue

            # Si el número está en la esq inferior derecha
            elif pos_num == (len(input_entrada[0]) - 1, len(input_entrada[1]) - 1):
                print(f'{num} en esq inferior derecha 489')
                # input("Stop en elif")
                # muevo el cero mientras el 0 no esté encima de num
                while pos_cero != (len(input_entrada[0]) - 2, len(input_entrada[1]) - 1):
                    mover_cercano(input_entrada[len(input_entrada[0]) - 2][len(input_entrada[1]) - 1])
                    pos_cero = buscar(input_entrada, 0)
                intercambiar(num)  # el 0 queda en esq inferior derecha
                # Muevo el 0 hasta la izquierda de num
                intercambiar(input_entrada[len(input_entrada[0]) - 1][len(input_entrada[1]) - 2])
                intercambiar(input_entrada[len(input_entrada[0]) - 2][len(input_entrada[1]) - 2])
                continue

            # Si el número está en la esquina inferior izda y el cero encima de num
            elif pos_num == (len(input_entrada[0]) - 1, 0) and pos_cero == (len(input_entrada[0]) - 2, 0):
                print("                 En elif nuevo ln:503   , pos_num:", pos_num)
                intercambiar(num)
                intercambiar(input_entrada[len(input_entrada[0]) - 1][1])
                continue

            #  Si el numero está a la derecha de pos_esperada y no está en ultima fila ni en la primera columna
            #  y además el cero está justo a la derecha de num
            elif pos_num[1] > pos_esperada[1] and pos_num[0] != (len(input_entrada[1]) - 1) \
                    and pos_num[1] != 0 and pos_cero == (pos_num[0], pos_num[1] + 1):
                input("Ojo entró en el else")
                print("Else en lin:523")
                rodearXdebajo_a_izquierda()
                continue

            # Si num está a la izda de pos_esperada y 0 justo a la izda de num y no es ultima fila
            elif pos_num[1] < pos_esperada[1] and pos_num == (pos_cero[0], pos_cero[1] + 1) \
                    and pos_num[0] != (len(input_entrada[1]) - 1):
                input("En ln 552")
                rodearXdebajo_a_derecha()
                continue

            # Si num esta en ultima fila y pos_esperada no, además 0 es colindate a num (misma fila)
            elif pos_num[0] == len(input_entrada[1]) - 1 and pos_esperada[0] != len(input_entrada[1]) - 1 \
                    and (pos_cero == (pos_num[0], pos_num[1] + 1) or pos_cero == (pos_num[0], pos_num[1] - 1)):
                print("else en lin 559 OJO QUE PASO AQUÍ")
                # todo importante algo cambié revisar elif(se quita?)
                input("Entró OJO QUE PASO AQUÍ")
                # Si num a la izda de pos_esperada y 0 a la dcha de num
                if pos_esperada[1] > pos_num[1] and pos_cero[1] > pos_num[1]:
                    print("intercambiar")
                    intercambiar(num)
                    continue
                # Si num a la izda de pos_esperada y 0 a la izda (lo subo una fila)
                elif pos_esperada[1] > pos_num[1]:
                    print("lo subo una fila")
                    intercambiar(input_entrada[pos_cero[0]-1][pos_cero[1]])
                    intercambiar(input_entrada[pos_cero[0]-1][pos_cero[1]+1])
                    intercambiar(input_entrada[pos_cero[0]][pos_cero[1]+1])
                    input("lo subo una fila ?????-¿¿¿ Lo quitamos???") # todo creo que sobra
                    continue

                # si num está bajo su posición: roto la fila para colocar num en su sitio y vuelvo a colocar la fila
                elif pos_num[1] == pos_esperada[1]:
                    input("            NUEVO ELIF")
                    while pos_cero[1] > 0:  # muevo 0 a primera columna
                        intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])
                        pos_cero = buscar(input_entrada, 0)
                    intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subo
                    pos_cero = buscar(input_entrada, 0)
                    while pos_cero[1] < pos_num[1]:  # Muevo 0 a derecha hasta pos_num[1]
                        intercambiar(input_entrada[pos_cero[0]][pos_cero[1] + 1])
                        pos_cero = buscar(input_entrada, 0)
                    pos_cero = buscar(input_entrada, 0)
                    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])  # Bajo ahora num está en su sitio
                    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]-1])  # Quito los que no van
                    intercambiar(input_entrada[pos_cero[0]][pos_cero[1]-1])
                    pos_cero = buscar(input_entrada, 0)
                    while pos_cero[1] > 0:  # muevo 0 a primera columna
                        intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])
                        pos_cero = buscar(input_entrada, 0)
                    intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])

            # Si el número está justo encima del 0 y pos_esperada está más arriba del número y 0 está en última columna
            elif pos_num == (pos_cero[0] - 1, pos_cero[1]) and pos_esperada[0] < pos_num[0] \
                    and pos_cero[1] == len(input_entrada[0]) - 1:
                print("Elif en linea:556")
                intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])
                intercambiar(input_entrada[pos_cero[0]-1][pos_cero[1] - 1])
                # intercambiar(input_entrada[pos_cero[0]-1][pos_cero[1]])
                continue

            # Si el número está justo encima del 0 y pos_esperada está más arriba del número y 0 no está en última columna
            elif pos_num == (pos_cero[0] - 1, pos_cero[1]) and pos_esperada[0] < pos_num[0]:
                print("Elif en linea:564")
                intercambiar(input_entrada[pos_cero[0]][pos_cero[1] + 1])
                continue

            # Su el número está justo a la derecha del 0 y num no está en la última fila ni última columna
            elif pos_num == (pos_cero[0], pos_cero[1] + 1) and pos_num[0] < len(input_entrada[1]) - 1 \
                    and pos_num[1] < len(input_entrada[0]) - 1:
                print("LN:571")
                rodearXdebajo_a_derecha()
                continue

            # El resto de opciones
            else:
                print("ULTIMO Else en lin:561")
                print(f'pos_esperada[0]: {pos_esperada[0]} != {len(input_entrada[1]) - 1} ->len(input_entrada[1])-1')
                mover_cercano(num)
                continue

        # num en su posición
        else:
            # print(f'Estamos en el else general El {num} está en su pocicion')
            num += 1
            print(f'****************Ahora num es: {num} *********************')

    print("\n!!! FELICIDADES, EL ROMPECABEZAS ESTÁ RESUELTO !!!")
    return 'OK'


def main():
    print("# Transiciones a realizar para resolver el rompecabezas:\n")
    if len(sys.argv) > 1:
        entrada = sys.argv
        entrada.remove(sys.argv[0])
        longitud = int(math.sqrt(len(entrada)))
        print(len(entrada), entrada, longitud)
        salida = str(entrada)
        array_entrada = np.empty((longitud+1, longitud+1))   # Creo el array bidimencional sin inicializar
        # print(len(entrada[0]))
        x, y = 0, 0
        for caracter in salida:
            if caracter.isnumeric():
                print(caracter,"posicion:",  x, y, "longitud", longitud)
                if x < longitud:
                    print(caracter)
                    if y <= longitud:
                        print(caracter,"posicion:",  x, y, "longitud", longitud)
                        array_entrada[x][y] = int(caracter) # todo no se porque aqui no se guarda bien, puede que
                        # sea al crearlo, comprobar con def res(entrada):
                        y += 1
                    else:
                        y = 0
                        x += 1

        print(array_entrada)
        input()
        # globals()['input_entrada'] = np.array([])
        # print("\nSALIDA:", salida)
        print(array_entrada)
    print("El array de entrada es:\n", input_entrada)
    posible = mover()
    if posible is None:
        print("---------------- SIN SOLUCIÓN ----------------")
        return None


if __name__ == '__main__':
    main()
