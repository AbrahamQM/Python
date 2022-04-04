#  Métodos de diferentes movimientos según posición y condiciones
import numpy as np

# Método que devuelve posiciones 'x' e 'y' del valor numero
def buscar(input_entrada, numero):
    for x in range(len(input_entrada)):
        for y in range(len(input_entrada)):
            if input_entrada[x][y] == numero:
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


def intercambiar(input_entrada, numero):
    cero = list(buscar(input_entrada, 0))
    indice = list(buscar(input_entrada, numero))
    input_entrada[cero[0]][cero[1]] = input_entrada[indice[0]][indice[1]]  # Asigno a la posición del 0 el número
    input_entrada[indice[0]][indice[1]] = 0  # Asigno en la posición del número el 0
    print("    |\n    V\n", input_entrada)


def comprobar_posicion(input_entrada, x, y, num):
    if (x, y) == buscar(input_entrada, num):  # Si num no está en su posición
        return True
    else:
        return False


def mover_cercano(input_entrada, num):
    if num == 9:
        pass
    pos_cero = buscar(input_entrada, 0)
    pos_num = buscar(input_entrada, num)
    if abs(pos_num[0] - pos_cero[0]) < abs(pos_num[1] - pos_cero[1]):  # Si se encuentra más cerca el eje x
        if pos_num[1] - pos_cero[1] > 0:  # si num está a la derecha del 0
            intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] + 1])
        elif pos_num[1] - pos_cero[1] < 0:  # si num está a la izquierda del 0
            intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] - 1])

    else:  # Si se encuentra más cerca del eje y o equidistante
        if (pos_num[0] - pos_cero[0]) < 0:  # si num está encima del 0
            intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])
        elif (pos_num[0] - pos_cero[0]) > 0:  # si num está debajo del 0
            intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])


def resuelto(input_entrada):  # Comprueba que el puzzle está resuelto (True) o no (False)
    esperado = res(input_entrada)
    for x in range(len(input_entrada)):
        for y in range(len(input_entrada)):
            if input_entrada[x][y] != esperado[x][y]:
                return False
    return True


def girar3_reloj(input_entrada, num):  # Método que hace girar en sentido de las agujas de reloj 3 posiciones
    pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] - 1])
    intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1] - 1])
    intercambiar(num)


def girar3_reloj_inv(input_entrada, num):  # Método que hace girar en sentido CONTRARIO a las agujas de reloj 3 posiciones
    pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])
    intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1] - 1])
    intercambiar(input_entrada, num)


#  Método que mueve el 0 por debajo del número
def rodearXdebajo_a_izquierda(input_entrada):
    pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])
    intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1] - 1])
    intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1] - 2])
    intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] - 2])


def rodearXdebajo_a_derecha(input_entrada):
    pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])
    intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1] + 1])
    intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1] + 2])
    intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] + 2])


# Método para resolver cuando num está en el extremo derecho del array debajo de su posición esperada
def cambiar_esquina(input_entrada):
    pos_cero = buscar(input_entrada, 0)
    while pos_cero[1] > 0:  # muevo 0 a izda
        intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] - 1])
        pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subo
    pos_cero = buscar(input_entrada, 0)
    while pos_cero[1] < len(input_entrada[0]) - 1:  # Muevo 0 a derecha
        intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] + 1])
        pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])
    intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1] - 1])
    intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] - 1])
    pos_cero = buscar(input_entrada, 0)
    while pos_cero[1] > 0:
        intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] - 1])
        pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])


#  Mueve el 0 hasta la primera columna
def mover_fila_a_derecha(input_entrada):
    pos_cero = buscar(input_entrada, 0)
    while pos_cero[1] != 0:
        intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] - 1])
        pos_cero = buscar(input_entrada, 0)


#  Mueve el 0 hasta la última columna
def mover_fila_a_izquierda(input_entrada):
    pos_cero = buscar(input_entrada, 0)
    while pos_cero[1] != len(input_entrada[1]) - 1:
        intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] + 1])
        pos_cero = buscar(input_entrada, 0)


#  Se encarga de la esquina derecha penúltima fila
def fila_penultima_derecha(input_entrada, num):
    pos_num_anterior = buscar(input_entrada, num -1)
    pos_num = buscar(input_entrada, num)
    pos_cero = buscar(input_entrada, 0)
    vueltas = 0
    while pos_num[1] <= pos_num_anterior[1]: # hasta que el número esté bajo su posición
        vueltas +=1
        if pos_cero[0] == len(input_entrada[1]) - 2:  # si el 0 está en la penúltima fila lo bajo
            intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])
        mover_fila_a_derecha(input_entrada)
        pos_num = buscar(input_entrada, num)
        pos_num_anterior = buscar(input_entrada, num - 1)
        if pos_num[1] >= pos_num_anterior[1]: # Para que pare cuando tengamos el número a la dcha del anterior
            break
        pos_cero = buscar(input_entrada, 0)
        intercambiar(input_entrada, input_entrada[pos_cero[0]-1][pos_cero[1]]) # subo el 0
        mover_fila_a_izquierda(input_entrada)
        pos_cero = buscar(input_entrada, 0)
        intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajo el 0
        pos_num = buscar(input_entrada, num)
        pos_num_anterior = buscar(input_entrada, num - 1)

    pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada, input_entrada[pos_cero[0]-1][pos_cero[1]]) # subo el 0
    pos_cero = buscar(input_entrada, 0)
    while pos_cero[1] != pos_num[1]: # muevo el 0 hasta que esté sobre el número
        intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1]+1])
        pos_num = buscar(input_entrada, num)
        pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada, input_entrada[pos_cero[0]+1][pos_cero[1]]) # bajo el 0
    intercambiar(input_entrada, input_entrada[pos_cero[0]+1][pos_cero[1]+1]) # 0 a dcha
    intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1]+1]) # subo 0

    mover_fila_a_derecha(input_entrada)
    intercambiar(input_entrada, input_entrada[len(input_entrada[1])-1][0]) # bajo el 0
    pos_num_anterior = buscar(input_entrada, num - 1)
    pos_cero = buscar(input_entrada, 0)
    while pos_cero[1] <= pos_num_anterior[1]: # Me coloco debajo del número que sobra
        intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1]+1])  #  0 a dcha
        pos_num_anterior = buscar(input_entrada, num - 1)
        pos_cero = buscar(input_entrada, 0)
    intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])  # subo 0 y quito el número que no va
    while pos_num_anterior != buscar(res(input_entrada), num - 1):  # recoloco los demás
        pos_cero = buscar(input_entrada, 0)
        if pos_cero[0] != len(input_entrada[1]) - 2:  # si el 0  no está en la penúltima fila ultima columna
            intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])  # lo subo
        mover_fila_a_derecha(input_entrada)
        intercambiar(input_entrada, input_entrada[len(input_entrada[1]) - 1][0])  # bajo el 0
        mover_fila_a_izquierda(input_entrada)
        pos_num_anterior = buscar(input_entrada, num - 1)


