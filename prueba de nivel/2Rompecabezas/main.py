# Rompecabezas deslizante

# Admite paso por parámetro del array o usar uno con el nombre input_entrada como los
# que he puesto a partir de la línea 13
# Soy consciente de que necesita refactorización ya que habrá bastante código redundante,
# pero lo entrego hasta el punto al que llegué.
import math
import numpy as np
import sys
import ultima_fila as u
# import ultimaFila as u
import metodos as m

# input entrada de ejemplo en la prueba
input_entrada = np.array([
  [1, 2, 3, 4],
  [5, 0, 6, 8],
  [9, 10, 7, 11],
  [13, 14, 15, 12]
])

# input_entrada = np.array([ # Con solución
#   [11, 10, 3, 7],
#   [4, 12, 2, 9],
#   [1, 8, 5, 15],
#   [13, 14, 0, 6]
# ])

# input_entrada = np.array([ # con solución
#      [0, 11, 10, 4],
#      [2, 3, 8, 7],
#      [1, 13, 15,9],
#      [6, 14, 5, 12]
# ])
# input_entrada = np.array([ # no tiene solución
#     [7, 1, 3, 4],
#     [5, 2, 6, 8],
#     [9, 10, 0, 11],
#     [13, 14, 15, 12]
# ])

# input_entrada = np.array([  # sin solución
#     [1, 2, 3],
#     [5, 4, 6],
#     [7, 0, 8]
# ])

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

# input_entrada = np.array([  # Con solución
#     [7, 1, 3, 4, 16],
#     [5, 2, 6, 8, 17],
#     [9, 10, 0, 11, 18],
#     [13, 14, 15, 12, 19],
#     [21, 22, 20, 23, 24]
# ])

# input_entrada = np.array([  # mas complicado aún
#     [7, 1, 3, 4, 16, 25],
#     [5, 2, 6, 8, 17, 27],
#     [9, 28, 10, 0, 11, 18],
#     [13, 14, 26, 15, 12, 19],
#     [21, 22, 20, 29, 23, 24],
#     [32, 30, 31, 34, 33, 35]
# ])

contador_stop = 0



def mover():
    num = 1  # Num actual a colocar se va incrementando
    ultima = 0
    while not m.resuelto(input_entrada):
        pos_cero = m.buscar(input_entrada, 0)
        pos_esperada = m.buscar(m.res(input_entrada), num)
        pos_num = m.buscar(input_entrada, num)
        if num == 12: # todo BORRAR
            pass
        # Si num no está en su posición pero si en su fila
        if not m.comprobar_posicion(input_entrada, pos_esperada[0], pos_esperada[1], num) and num in input_entrada[pos_esperada[0]]:
            if ultima == None:
                return ultima
            # Si num es colindante al 0 y el 0 está en la misma fila que num
            if (pos_num == (pos_esperada[0], pos_esperada[1] + 1) or pos_num == (
                    pos_esperada[0] + 1, pos_esperada[1]) or pos_num == (pos_esperada[0] - 1, pos_esperada[1]) or
                pos_num == (pos_esperada[0], pos_esperada[1] - 1)) and pos_cero[0] == pos_num[0]:

                # Si el cero está a la izda de num y hay que mover num a izda
                if pos_cero[1] < pos_num[1] and pos_esperada[1] < pos_num[1]:
                    m.intercambiar(input_entrada, num)
                    continue

                # Si el 0 está a la derecha de num y hay que mover a la izda y no estamos en la última fila
                elif pos_cero[1] > pos_num[1] > pos_esperada[1] and pos_cero[0] < len(input_entrada[1]) - 1:
                    m.rodearXdebajo_a_izquierda(input_entrada)
                    continue
            #  num no es colindante a 0 y el numero está es la esquina superior-izda del 0
            if pos_cero[0] - 1 == pos_num[0] and pos_cero[1] - 1 == pos_num[1]:
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_num[1]])  # movemos el 0 a su izquierda 1 posición
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_num[1] - 1])  # movemos el 0 a su izquierda 2 posición
                m.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_num[1] - 1])  # movemos el 0 arriba
                continue

            # Si num está en la misma fila que el 0 pero no es colindante y pos_esperada no está en la última fila
            elif pos_cero[0] == pos_num[0] and pos_cero[1] != pos_num[1] - 1 and pos_cero[1] != pos_num[1] + 1 \
                    and pos_esperada[0] < len(input_entrada[1]) - 1:
                m.mover_cercano(input_entrada, num)
                continue

            # Si num es colindante al cero,
            elif (pos_cero == (pos_num[0], pos_num[1] + 1) or pos_cero == (pos_num[0] + 1, pos_num[1])
                  or pos_cero == (pos_num[0] - 1, pos_num[1])
                  or pos_cero == (pos_num[0], pos_num[1] - 1)):

                if pos_num[0] == 0 and pos_num[1] != 0:  # Si el número está en la fila superior pero no en columna 0
                    m.girar3_reloj(input_entrada, num)
                    continue

                # Si num está JUSTO a la derecha del 0 y pos_esperada está a la izquierda
                elif pos_num == (pos_cero[0], pos_cero[1] + 1) and pos_esperada[1] < pos_num[1]:
                    m.intercambiar(input_entrada, num)
                    continue

                # Si num está JUSTO a la izquierda del 0 y pos_esperada está a la izquierda de num y no es última fila
                elif pos_num == (pos_cero[0], pos_cero[1] - 1) and pos_esperada[1] < pos_num[1] \
                        and pos_num[0] < len(input_entrada[1]) - 1:
                    m.rodearXdebajo_a_izquierda(input_entrada)
                    continue

                # si pos_esperada está en la última fila
                elif pos_esperada[0] == len(input_entrada[1]) - 1 and ultima != None:
                    if len(input_entrada[0]) > 3:
                        ultima = u.ultima_fila(input_entrada, num)
                        continue
                    else:
                        return None

                # Si el número está JUSTO encima del 0 y no es la primera columna
                elif pos_num == (pos_cero[0] - 1, pos_cero[1]) and pos_num[1] != 0:  # Lo rodeo hasta su izda
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] - 1])
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1] - 1])
                    continue

            # si pos_esperada está en la última fila
            elif pos_esperada[0] == len(input_entrada[1]) - 1 and ultima != None:
                if len(input_entrada[0]) > 3:
                    ultima = u.ultima_fila(input_entrada, num)
                    continue
                else:
                    return None

            else:  # Si num no es colindante a 0, ni están en la misma fila
                m.mover_cercano(input_entrada, num)
                continue

        # Si num no está en su posición ni en su fila
        elif not m.comprobar_posicion(input_entrada, pos_esperada[0], pos_esperada[1], num) and num not in input_entrada[
            pos_esperada[0]]:

            # Si es colindante al 0 y el num no está en la columna esperada y el cero está a la izq de num
            if (pos_cero == (pos_num[0], pos_num[1] + 1) or pos_cero == (pos_num[0] + 1, pos_num[1])
                or pos_cero == (pos_num[0] - 1, pos_num[1]) or pos_cero == (pos_num[0], pos_num[1] - 1)) \
                    and pos_num[1] != pos_esperada[1] and pos_num[1] > pos_cero[1]:

                # El 0 está justo a la izda de num y la columna esperada a la derecha de num y no es última fila
                if pos_cero == (pos_num[0], pos_num[1] - 1) and pos_esperada[1] > pos_num[1] \
                        and pos_num[0] != len(input_entrada[1]) - 1:
                    m.rodearXdebajo_a_derecha(input_entrada)
                    continue

                # Si no está en la última fila
                elif pos_num[0] != len(input_entrada[1]) - 1:
                    m.intercambiar(input_entrada, num)
                    continue

                # Si num está en la última fila pero pos_esperada no
                elif pos_esperada[0] != len(input_entrada[1]) - 1:
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1] + 1])
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] + 1])
                    continue

            # 0 esta a la derecha de num, numero esta debajo de pos_esperada, num está en la columna esperada,
            # la columna esperada no es la última
            elif pos_cero == (pos_num[0], pos_num[1] + 1) and pos_num[0] > pos_esperada[0] and \
                    pos_num[1] == pos_esperada[1] and pos_esperada[1] < len(input_entrada[1] - 1):
                m.girar3_reloj_inv(input_entrada, num)
                continue

            # 0 está sobre el num y pos_esperada es la del 0
            elif pos_cero == (pos_num[0] - 1, pos_num[1]) and pos_esperada == pos_cero:
                m.intercambiar(input_entrada, num)
                continue

            # todo cambiado, copia debajo----Pero Si 0 está justo a izda de num, num está en la columna esperada, la columna no es la última y el 0 no
            # está encima del num y no está en última fila
            elif pos_cero == (pos_num[0], pos_num[1] - 1) \
                    and pos_num[0] > pos_esperada[0] and pos_num[1] == pos_esperada[1] \
                    and pos_esperada[1] < len(input_entrada[1]) - 1 and pos_cero[0] >= pos_num[0] \
                    and pos_num[0] != len(input_entrada[0]) - 1: # todo cambio pos_cero[0] <= pos_num[0] x >=
                # Pero Si es colindante al 0, num está en la columna esperada, la columna no es la última y el 0 no
                # está encima del num y no está en última fila
# #           elif ((pos_cero == (pos_num[0], pos_num[1] + 1) or pos_cero == (pos_num[0] + 1, pos_num[1])
#                    or pos_cero == (pos_num[0] - 1, pos_num[1]) or pos_cero == (pos_num[0], pos_num[1] - 1))) \
#                     and pos_num[0] > pos_esperada[0] and pos_num[1] == pos_esperada[1] \
#                     and pos_esperada[1] < len(input_entrada[1]) - 1 and pos_cero[0] >= pos_num[0] \
#                     and pos_num[0] != len(input_entrada[0]) - 1: # todo cambio pos_cero[0] <= pos_num[0] x >=
                m.rodearXdebajo_a_derecha(input_entrada)
                m.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1] + 2])
                m.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1] + 1])
                continue

            # Pero Si es colindante al 0, num esta en la columna esperada, la columna SI es la última y el 0 no
            # está encima del num
            elif ((pos_cero == (pos_num[0], pos_num[1] + 1) or pos_cero == (pos_num[0] + 1, pos_num[1])
                   or pos_cero == (pos_num[0] - 1, pos_num[1]) or pos_cero == (pos_num[0], pos_num[1] - 1))) \
                    and pos_num[0] > pos_esperada[0] and pos_num[1] == pos_esperada[1] \
                    and pos_esperada[1] == len(input_entrada[1]) - 1 and pos_cero[0] >= pos_num[0]:

                # Si num no está JUSTO debajo de pos_esperada y cero justo a la izda de num
                if pos_num != (pos_esperada[0] + 1, pos_esperada[1]) and pos_cero == (pos_num[0], pos_num[1] - 1):
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1] + 1])
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] + 1])
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1]])
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])
                    continue

                # Si su posición esperada es justo encima de donde está y el 0 está a en la misma fila de num
                elif pos_esperada == (pos_num[0] - 1, pos_num[1]) and pos_cero[0] == pos_num[0]:
                    m.cambiar_esquina(input_entrada)
                    continue

            # Si el num esta a la izda de su posición, el 0 a la izda del num
            elif pos_num[1] < pos_esperada[1] and pos_cero == (pos_num[0], pos_num[1] -1) : # todo cambios con el 3 aquí
                m.rodearXdebajo_a_derecha(input_entrada)
                continue

            # Si el número está en la esq inferior derecha
            elif pos_num == (len(input_entrada[0]) - 1, len(input_entrada[1]) - 1):
                # muevo el cero mientras el 0 no esté encima de num
                while pos_cero != (len(input_entrada[0]) - 2, len(input_entrada[1]) - 1):
                    m.mover_cercano(input_entrada, input_entrada[len(input_entrada[0]) - 2][len(input_entrada[1]) - 1])
                    pos_cero = m.buscar(input_entrada, 0)
                m.intercambiar(input_entrada, num)  # el 0 queda en esq inferior derecha
                # Muevo el 0 hasta la izquierda de num
                m.intercambiar(input_entrada, input_entrada[len(input_entrada[0]) - 1][len(input_entrada[1]) - 2])
                m.intercambiar(input_entrada, input_entrada[len(input_entrada[0]) - 2][len(input_entrada[1]) - 2])
                continue

            # Si el número está en la esquina inferior izda y el cero encima de num
            elif pos_num == (len(input_entrada[0]) - 1, 0) and pos_cero == (len(input_entrada[0]) - 2, 0):
                m.intercambiar(input_entrada, num)
                m.intercambiar(input_entrada, input_entrada[len(input_entrada[0]) - 1][1])
                continue

            #  Si el numero está a la derecha de pos_esperada y no está en última fila ni en la primera columna
            #  y además el cero está justo a la derecha de num
            elif pos_num[1] > pos_esperada[1] and pos_num[0] != (len(input_entrada[1]) - 1) \
                    and pos_num[1] != 0 and pos_cero == (pos_num[0], pos_num[1] + 1):
                m.rodearXdebajo_a_izquierda(input_entrada)
                continue

            # Si num está a la izda de pos_esperada y 0 justo a la izda de num y no es ultima fila
            elif pos_num[1] < pos_esperada[1] and pos_num == (pos_cero[0], pos_cero[1] + 1) \
                    and pos_num[0] != (len(input_entrada[1]) - 1):
                m.rodearXdebajo_a_derecha(input_entrada)
                continue

            # Si num esta en ultima fila y pos_esperada no, además 0 es colindate a num (misma fila)
            elif pos_num[0] == len(input_entrada[1]) - 1 and pos_esperada[0] != len(input_entrada[1]) - 1 \
                    and (pos_cero == (pos_num[0], pos_num[1] + 1) or pos_cero == (pos_num[0], pos_num[1] - 1)):

                # Si num a la izda de pos_esperada y 0 a la dcha de num
                if pos_esperada[1] > pos_num[1] and pos_cero[1] > pos_num[1]:
                    m.intercambiar(input_entrada, num)
                    continue

                # Si num a la izda de pos_esperada y 0 a la izda (lo subo una fila)
                elif pos_esperada[1] > pos_num[1]:
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1] + 1])
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] + 1])
                    continue

                # Si num está en su columna y es un array 3x3
                elif pos_num[1] == pos_esperada[1] and len(input_entrada[0]) == 3:
                    while pos_cero[1] > 0:  # muevo 0 a primera columna
                        m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] - 1])
                        pos_cero = m.buscar(input_entrada, 0)
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subo
                    pos_cero = m.buscar(input_entrada, 0)
                    while pos_cero[1] < pos_num[1]:  # Muevo 0 a derecha hasta pos_num[1]
                        m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] + 1])
                        pos_cero = m.buscar(input_entrada, 0)
                    pos_cero = m.buscar(input_entrada, 0)
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])  # Bajo ahora num está en su sitio
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1] + 1])  # muevo 0 hasta la derecha
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] + 1])  # subo 0
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1]])  # muevo 0 a izda
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] - 1])  # muevo 0 a izda
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1] - 1])  # bajo 0 y coloco el numero anterior
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])  # lo coloco bajo la posicion de num
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1]])  #
                    continue

                # si num está bajo su posición y no es un array de 3x3
                # roto la fila para colocar num en su sitio y vuelvo a colocar la fila
                elif pos_num[1] == pos_esperada[1]:
                    while pos_cero[1] > 0:  # muevo 0 a primera columna
                        m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] - 1])
                        pos_cero = m.buscar(input_entrada, 0)
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subo
                    pos_cero = m.buscar(input_entrada, 0)
                    while pos_cero[1] < pos_num[1]:  # Muevo 0 a derecha hasta pos_num[1]
                        m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] + 1])
                        pos_cero = m.buscar(input_entrada, 0)
                    pos_cero = m.buscar(input_entrada, 0)
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])  # Bajo ahora num está en su sitio
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1] - 1])  # Quito los que no van
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] - 1])
                    pos_cero = m.buscar(input_entrada, 0)
                    while pos_cero[1] > 0:  # muevo 0 a primera columna
                        m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] - 1])
                        pos_cero = m.buscar(input_entrada, 0)
                    m.intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])
                    continue

            # Si el número está justo encima del 0 y pos_esperada está más arriba del número y 0 está en última columna
            elif pos_num == (pos_cero[0] - 1, pos_cero[1]) and pos_esperada[0] < pos_num[0] \
                    and pos_cero[1] == len(input_entrada[0]) - 1:
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] - 1])
                m.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1] - 1])
                continue

        # Si el número está justo encima del 0 y pos_esperada está más arriba del número y 0 no está en última columna
            elif pos_num == (pos_cero[0] - 1, pos_cero[1]) and pos_esperada[0] < pos_num[0]:
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] + 1])
                continue

            # Su el número está justo a la derecha del 0 y num no está en la última fila ni última columna
            elif pos_num == (pos_cero[0], pos_cero[1] + 1) and pos_num[0] < len(input_entrada[1]) - 1 \
                    and pos_num[1] < len(input_entrada[0]) - 1:
                m.rodearXdebajo_a_derecha(input_entrada)
                continue

            # Si el numero esta a la izquierda de columna esperada y columna esperada es la 2º columna y
            # el 0 está en la posición esperada (en la penúltima fila)
            elif pos_num[1] < pos_esperada[1] and pos_esperada[1] == 1 and pos_cero == pos_esperada \
                and pos_esperada[0] == len(input_entrada[1]) -2:
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] + 1])
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]+1][pos_cero[1] + 1])
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]+1][pos_cero[1]])
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]+1][pos_cero[1]-1])
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1]-1])
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1]])
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]+1][pos_cero[1]])
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]+1][pos_cero[1]+1])
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1]+1])
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1]])
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1]-1])
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]+1][pos_cero[1]-1])
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]+1][pos_cero[1]])
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1]])
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1]+1])
                continue

            # Si pos_esperada es en penúltima fila, última columna Y no es un array de 3x3
            elif pos_esperada == (len(input_entrada[0])-2, len(input_entrada[1])-1) and len(input_entrada[1]) > 3: # todo ponerlo como un método o fichero diferente
                m.fila_penultima_derecha(input_entrada, num)
                continue

            # si el 0 está en la posición esperada y num más abajo
            elif pos_cero[0] < pos_num[0] and pos_cero == pos_esperada:
                m.intercambiar(input_entrada, input_entrada[pos_cero[0]+1][pos_cero[1]])# bajo el 0
                continue


            # El resto de opciones
            else:
                m.mover_cercano(input_entrada, num)
                continue

        # num en su posición
        else:
            num += 1
            # print(f'****************Ahora num es: {num} *********************')

    print("\n!!! FELICIDADES, EL ROMPECABEZAS ESTÁ RESUELTO !!!")
    return 'OK'


def main():
    print("# Transiciones a realizar para resolver el rompecabezas:\n")
    if len(sys.argv) > 1: # si hemos introducido el array por comando (parámetro)
        entrada = sys.argv
        entrada.remove(sys.argv[0])
        entrada = str(entrada)
        temporal = []
        i = 0
        for x in range(len(entrada)-1): # obtengo los elementos del array obviando los caracteres
            if i == x:
                if entrada[i].isnumeric():
                    if entrada[i+1].isnumeric():
                        temporal.append(entrada[i] + entrada[i+1])
                        i = x + 2
                    else:
                        temporal.append(entrada[i])
                        i = x + 1
                else:
                    i = x + 1

        longitud = int(math.sqrt(len(temporal)) -1)

        # Reinicio input entrada con el array bidimensional sin inicializar
        globals()['input_entrada'] = np.empty((longitud+1, longitud+1), int)
        x, y = 0, 0
        # for caracter in entrada:
        for numero in temporal:  # asigno los elementos en sus posiciones dentro del array
            if x <= longitud:
                if y <= longitud:
                    globals()['input_entrada'][x][y] = int(numero)
                    y += 1
                else:
                    y = 0
                    x += 1
                    globals()['input_entrada'][x][y] = int(numero)
                    y += 1

    print("El array de entrada es:\n", input_entrada)
    posible = mover()
    if posible is None:
        print("---------------- SIN SOLUCIÓN ----------------")
        return None


if __name__ == '__main__':
    main()
