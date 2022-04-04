import metodos as me
import ultimaFila2 as u


def ultima_fila(entrada, num):
    input_entrada = entrada
    res_esperado = me.res(input_entrada)
    sig = num + 1
    pos_sig = me.buscar(input_entrada, sig)
    pos_esperada = me.buscar(me.res(input_entrada), num)
    pos_num = me.buscar(input_entrada, num)

    # Si el siguiente numero está a la izda de num y input_entrada es más de 4x4
    if pos_num[1] > pos_sig[1] and len(input_entrada[0]) > 4:
        # hasta que num esté a la derecha del siguiente (aunque sea en otra fila)
        while pos_num[1] > pos_sig[1]:
            me.mover_fila_a_derecha(input_entrada)
            pos_cero = me.buscar(input_entrada, 0)
            me.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
            me.mover_fila_a_izquierda(input_entrada)
            pos_cero = me.buscar(input_entrada, 0)
            me.intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])  # Bajar fila (misma columna)
            pos_num = me.buscar(input_entrada, num)
            pos_sig = me.buscar(input_entrada, sig)

        pos_cero = me.buscar(input_entrada, 0)
        while pos_cero[1] != pos_num[1]:  # Hasta que el 0 esté bajo num
            me.intercambiar(input_entrada, input_entrada[pos_cero[0]][pos_cero[1] - 1])
            pos_num = me.buscar(input_entrada, num)
            pos_cero = me.buscar(input_entrada, 0)
        me.intercambiar(input_entrada, input_entrada[pos_cero[0] - 1][pos_cero[1]])
        me.mover_fila_a_derecha(input_entrada)
        pos_cero = me.buscar(input_entrada, 0)
        me.intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])
        me.mover_fila_a_izquierda(input_entrada)

        # recolocamos
        pos_cero = me.buscar(input_entrada, 0)
        pos_num = me.buscar(input_entrada, num)
        while pos_num != pos_esperada:
            me.intercambiar(input_entrada, input_entrada[pos_cero[0]-1][pos_cero[1]])
            me.mover_fila_a_derecha(input_entrada)
            pos_cero = me.buscar(input_entrada, 0)
            me.intercambiar(input_entrada, input_entrada[pos_cero[0] + 1][pos_cero[1]])
            me.mover_fila_a_izquierda(input_entrada)
            pos_num = me.buscar(input_entrada, num)
            pos_cero = me.buscar(input_entrada, 0)
        return True
    else:
        if len(input_entrada[0]) > 3:
            ultima = u.ultima_fila(input_entrada, num)
            if ultima == None:
                return None
            else:
                return True


