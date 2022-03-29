import main as m


def ultima_fila(entrada, num):
    input_entrada = entrada
    res_esperado = m.res(input_entrada)
    pos_esperada = m.buscar(m.res(input_entrada), num)
    ultimo_cuadrante = [(len(input_entrada[0]) - 2, len(input_entrada[1]) - 2),
                        (len(input_entrada[0]) - 2, len(input_entrada[1]) - 1),
                        (len(input_entrada[0]) - 1, len(input_entrada[1]) - 2),
                        (len(input_entrada[0]) - 1, len(input_entrada[1]) - 1)]

    if num != int(res_esperado.max()): # para ver si hay 1 o 2 numeros más
        sig1 = num + 1
        if sig1 != int(res_esperado.max()):
            sig2 = num + 2
        else:
            sig2 = 0
    else:
        sig1 = 0

    def intercambiar(numero): # lo tengo que duplicar para que siga trabajando con el array o tendría que cambiar todo
        cero = list(m.buscar(input_entrada, 0))
        indice = list(m.buscar(input_entrada, numero))
        input_entrada[cero[0]][cero[1]] = input_entrada[indice[0]][indice[1]]  # Asigno a la posición del 0 el número
        input_entrada[indice[0]][indice[1]] = 0  # Asigno en la posición del número el 0
        print("    |\n    V\n", input_entrada)

    def mover_fila_a_derecha():
        pos_cero = m.buscar(input_entrada, 0)
        while pos_cero[1] != 0:
            intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])
            pos_cero = m.buscar(input_entrada, 0)

    def mover_fila_a_izquierda():
        pos_cero = m.buscar(input_entrada, 0)
        while pos_cero[1] != len(input_entrada[1]) - 1:
            intercambiar(input_entrada[pos_cero[0]][pos_cero[1] + 1])
            pos_cero = m.buscar(input_entrada, 0)

    def rotar4(): # gira cuatro números el 0 debe star en la esq inferior-izq de los 4 números
        pos_cero = m.buscar(input_entrada, 0)
        intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
        intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1] + 1])  # Mover a derecha
        intercambiar(input_entrada[pos_cero[0]][pos_cero[1] + 1])  # Bajar fila (misma columna)
        intercambiar(input_entrada[pos_cero[0]][pos_cero[1]])  # Vuelve a pos inicial

    # ROTAMOS LAS DOS ÚLTIMAS FILAS hasta que num, sig1 y sig2(en caso de haberlo) estén en la esquina inferior derecha
    def cuadrar_esquina():
        pos_num = m.buscar(input_entrada, num)
        if sig2 != 0:
            pos_sig1 = m.buscar(input_entrada, sig1)
            pos_sig2 = m.buscar(input_entrada, sig2)
            # hasta que num y los 2 siguientes no estén en el último cuadrante:
            while pos_sig2 not in ultimo_cuadrante or pos_sig1 not in ultimo_cuadrante \
                    or pos_num not in ultimo_cuadrante:  # todo cambio or por and DESAGO EL CAMBIO
                mover_fila_a_derecha()
                pos_cero = m.buscar(input_entrada, 0)
                intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
                mover_fila_a_izquierda()
                pos_cero = m.buscar(input_entrada, 0)
                intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar 0 (misma columna)
                pos_num = m.buscar(input_entrada, num)
                pos_sig1 = m.buscar(input_entrada, sig1)
                pos_sig2 = m.buscar(input_entrada, sig2)

        elif sig1 != 0:
            pos_sig1 = m.buscar(input_entrada, sig1)
            # hasta que num y el siguiente no estén en el último cuadrante:
            while pos_sig1 not in ultimo_cuadrante or pos_num not in ultimo_cuadrante:  # todo cambio or por and DESAGO EL CAMBIO
                mover_fila_a_derecha()
                pos_cero = m.buscar(input_entrada, 0)
                intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
                mover_fila_a_izquierda()
                pos_cero = m.buscar(input_entrada, 0)
                intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar 0 (misma columna)
                pos_num = m.buscar(input_entrada, num)
                pos_sig1 = m.buscar(input_entrada, sig1)

        else:
            # hasta que num no esté en el ultimo_cuadrante
            while pos_num not in ultimo_cuadrante:
                mover_fila_a_derecha()
                pos_cero = m.buscar(input_entrada, 0)
                intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
                mover_fila_a_izquierda()
                pos_cero = m.buscar(input_entrada, 0)
                intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar 0 (misma columna)
                pos_num = m.buscar(input_entrada, num)

    cuadrar_esquina()  # coloco num y los 2 siguientes (si los hay) en el ultimo cuadrante y los ordeno
    pos_num = m.buscar(input_entrada, num)
    giros = 0
    if sig2 != 0:
        pos_sig2 = m.buscar(input_entrada, sig2)
        pos_sig1 = m.buscar(input_entrada, sig1)
        pos_cero = m.buscar(input_entrada, 0)
        intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])
        while (pos_num != ultimo_cuadrante[0] or pos_sig1 != ultimo_cuadrante[3] or pos_sig2 != ultimo_cuadrante[1]) \
                and giros < 6:  # todo cambio aquí cambio and por or en paréntesis
            input("En if de ultima_fila")
            rotar4()
            giros += 1
            pos_num = m.buscar(input_entrada, num)
            pos_sig1 = m.buscar(input_entrada, sig1)
            pos_sig2 = m.buscar(input_entrada, sig2)

    elif sig1 != 0:
        pos_sig1 = m.buscar(input_entrada, sig1)
        # Mientras num no esté en (última fila) (ultima columna -1) y sig1 en esq inferior derecha y giros < 6
        while (pos_num != ultimo_cuadrante[2] and pos_sig1 != ultimo_cuadrante[3]) and giros < 6:
            pos_cero = m.buscar(input_entrada, 0)
            if pos_cero[1] > 0:  # si 0 no está en la primera columna
                intercambiar(input_entrada[pos_cero[0]][pos_cero[1] - 1])  # lo muevo a la izquierda una posición
            else:
                return None

            rotar4()
            giros += 1
            pos_num = m.buscar(input_entrada, num)
            pos_sig1 = m.buscar(input_entrada, sig1)
            continue

    if giros < 6:
        pos_cero = m.buscar(input_entrada, 0)
        intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
        pos_num = m.buscar(input_entrada, num)
        while pos_num != pos_esperada:
            mover_fila_a_derecha()
            pos_cero = m.buscar(input_entrada, 0)
            intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar fila (misma columna)
            mover_fila_a_izquierda()
            pos_cero = m.buscar(input_entrada, 0)
            intercambiar(input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
            pos_num = m.buscar(input_entrada, num)

        pos_cero = m.buscar(input_entrada, 0)
        intercambiar(input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar fila (misma columna)
    else:
        return None
