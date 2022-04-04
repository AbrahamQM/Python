import metodos as me
# Método para cuando num está a la derecha del siguiente


def ultima_fila(entrada, num):
    input_entrada = entrada
    res_esperado = me.res(input_entrada)
    sig1, sig2 = 0, 0
    pos_esperada = me.buscar(me.res(input_entrada), num)
    ultimo_cuadrante = [(len(input_entrada[0]) - 2, len(input_entrada[1]) - 2),
                        (len(input_entrada[0]) - 2, len(input_entrada[1]) - 1),
                        (len(input_entrada[0]) - 1, len(input_entrada[1]) - 2),
                        (len(input_entrada[0]) - 1, len(input_entrada[1]) - 1)]

    if num != int(res_esperado.max()): # para ver si hay 1 o 2 numeros más
        sig1 = num + 1
        if sig1 != int(res_esperado.max()):
            sig2 = num + 2


    def rotar4(): # gira cuatro números el 0 debe star en la esq inferior-izq de los 4 números
        pos_cero = me.buscar(input_entrada, 0)
        me.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
        me.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1] + 1])  # Mover a derecha
        me.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] + 1])  # Bajar fila (misma columna)
        me.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1]])  # Vuelve a pos inicial

    # ROTAMOS LAS DOS ÚLTIMAS FILAS hasta que num, sig1 y sig2(en caso de haberlo) estén en la esquina inferior derecha
    def cuadrar_esquina():
        pos_num = me.buscar(input_entrada, num)
        if sig2 != 0 and sig2 == int(res_esperado.max()):
            input("Entró aqui 32")
            pos_sig1 = me.buscar(input_entrada, sig1)
            pos_sig2 = me.buscar(input_entrada, sig2)
            # hasta que num y los 2 siguientes no estén en el último cuadrante:
            while pos_sig2 not in ultimo_cuadrante or pos_sig1 not in ultimo_cuadrante \
                    or pos_num not in ultimo_cuadrante:
                me.mover_fila_a_derecha(input_entrada)
                pos_cero = me.buscar(input_entrada, 0)
                me.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
                me.mover_fila_a_izquierda(input_entrada)
                pos_cero = me.buscar(input_entrada, 0)
                me.intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar 0 (misma columna)
                pos_num = me.buscar(input_entrada, num)
                pos_sig1 = me.buscar(input_entrada, sig1)
                pos_sig2 = me.buscar(input_entrada, sig2)

        elif sig1 != 0 and sig2 == 0:
            pos_sig1 = me.buscar(input_entrada, sig1)
            # hasta que num y el siguiente no estén en el último cuadrante:
            while pos_sig1 not in ultimo_cuadrante or pos_num not in ultimo_cuadrante:
                me.mover_fila_a_derecha(input_entrada)
                pos_cero = me.buscar(input_entrada, 0)
                me.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
                me.mover_fila_a_izquierda(input_entrada)
                pos_cero = me.buscar(input_entrada, 0)
                me.intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar 0 (misma columna)
                pos_num = me.buscar(input_entrada, num)
                pos_sig1 = me.buscar(input_entrada, sig1)

        else:
            # hasta que num no esté en el ultimo_cuadrante
            input("Entro en ln 63")
            while pos_num not in ultimo_cuadrante:
                me.mover_fila_a_derecha(input_entrada)
                pos_cero = me.buscar(input_entrada, 0)
                me.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
                me.mover_fila_a_izquierda(input_entrada)
                pos_cero = me.buscar(input_entrada, 0)
                me.intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar 0 (misma columna)
                pos_num = me.buscar(input_entrada, num)
            input("salgo en 70")

    cuadrar_esquina()  # coloco num y los 2 siguientes (si los hay) en el ultimo cuadrante y los ordeno
    pos_num = me.buscar(input_entrada, num)
    giros = 0
    if sig2 != 0:
        pos_sig2 = me.buscar(input_entrada, sig2)
        pos_sig1 = me.buscar(input_entrada, sig1)
        pos_cero = me.buscar(input_entrada, 0)
        me.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] - 1])
        while (pos_num != ultimo_cuadrante[0] or pos_sig1 != ultimo_cuadrante[3] or pos_sig2 != ultimo_cuadrante[1]) \
                and giros < 6:
            rotar4()
            giros += 1
            pos_num = me.buscar(input_entrada, num)
            pos_sig1 = me.buscar(input_entrada, sig1)
            pos_sig2 = me.buscar(input_entrada, sig2)

    elif sig1 != 0:
        pos_sig1 = me.buscar(input_entrada, sig1)
        # Mientras num no esté en (última fila) (ultima columna -1) y sig1 en esq inferior derecha y giros < 6
        while (pos_num != ultimo_cuadrante[2] and pos_sig1 != ultimo_cuadrante[3]) and giros < 6:
            pos_cero = me.buscar(input_entrada, 0)
            if pos_cero[1] > 0:  # si 0 no está en la primera columna
                me.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] - 1])  # lo muevo a la izquierda una posición
            else:
                return None

            rotar4()
            giros += 1
            pos_num = me.buscar(input_entrada, num)
            pos_sig1 = me.buscar(input_entrada, sig1)
            continue


    if giros < 6:
        pos_cero = me.buscar(input_entrada, 0)
        me.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
        pos_num = me.buscar(input_entrada, num)
        while pos_num != pos_esperada:
            me.mover_fila_a_derecha(input_entrada)
            pos_cero = me.buscar(input_entrada, 0)
            me.intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar fila (misma columna)
            me.mover_fila_a_izquierda(input_entrada)
            pos_cero = me.buscar(input_entrada, 0)
            me.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
            pos_num = me.buscar(input_entrada, num)

        pos_cero = me.buscar(input_entrada, 0)
        me.intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar fila (misma columna)
    else:
        return None
