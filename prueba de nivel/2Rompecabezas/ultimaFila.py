import main as m

def ultima_fila(num):
    res_esperado = m.res(m.input_entrada)
    pos_esperada = m.buscar(m.res(m.input_entrada), num)
    # pos_num = buscar(input_entrada, num)
    ultimo_cuadrante = [(len(m.input_entrada[0]) - 2, len(m.input_entrada[1]) - 2),
                        (len(m.input_entrada[0]) - 2, len(m.input_entrada[1]) - 1),
                        (len(m.input_entrada[0]) - 1, len(m.input_entrada[1]) - 2),
                        (len(m.input_entrada[0]) - 1, len(m.input_entrada[1]) - 1)]

    if num != int(res_esperado.max()):
        # print("hay un número más")
        sig1 = num + 1
        # pos_sig1 = buscar(input_entrada, sig1)
        if sig1 != int(res_esperado.max()):
            sig2 = num + 2
            # pos_sig2 = buscar(input_entrada, sig2)
            # print("hay dos números más")
        else:
            sig2 = 0
    else:
        sig1 = 0

    # print("Entrada:\n", input_entrada)

    def mover_fila_a_derecha():
        # print("*******Mover_fila_a_derecha()********")
        pos_cero = m.buscar(m.input_entrada, 0)
        while pos_cero[1] != 0:
            m.intercambiar(m.input_entrada[pos_cero[0]][pos_cero[1] - 1])
            # print(input_entrada)
            pos_cero = m.buscar(m.input_entrada, 0)
        # print("///Fin mover_fila_a_derecha")

    def mover_fila_a_izquierda():
        # print("*******Mover_fila_a_izquierda()********")
        pos_cero = m.buscar(m.input_entrada, 0)
        while pos_cero[1] != len(m.input_entrada[1]) - 1:
            m.intercambiar(m.input_entrada[pos_cero[0]][pos_cero[1] + 1])
            # print(input_entrada)
            pos_cero = m.buscar(m.input_entrada, 0)
        # print("///Fin mover_fila_a_izquierda")

    def rotar4():
        pos_cero = m.buscar(m.input_entrada, 0)
        m.intercambiar(m.input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
        m.intercambiar(m.input_entrada[pos_cero[0] - 1][pos_cero[1] + 1])  # Mover a derecha
        m.intercambiar(m.input_entrada[pos_cero[0]][pos_cero[1] + 1])  # Bajar fila (misma columna)
        m.intercambiar(m.input_entrada[pos_cero[0]][pos_cero[1]])  # Vuelve a pos inicial
        # print("                                 -----FIn de rotar4------")

    # ROTAMOS LAS DOS ÚLTIMAS FILAS hasta que num, sig1 y sig2(en caso de haberlo) estén en la esquina inferior derecha
    def cuadrar_esquina():
        pos_num = m.buscar(m.input_entrada, num)
        if sig2 != 0:
            pos_sig1 = m.buscar(m.input_entrada, sig1)
            pos_sig2 = m.buscar(m.input_entrada, sig2)
            # hasta que num y los 2 siguientes no estén en el último cuadrante:
            while pos_sig2 not in ultimo_cuadrante and pos_sig1 not in ultimo_cuadrante \
                    and pos_num not in ultimo_cuadrante:  # todo cambio or por and
                mover_fila_a_derecha()
                pos_cero = m.buscar(m.input_entrada, 0)
                m.intercambiar(m.input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
                mover_fila_a_izquierda()
                pos_cero = m.buscar(m.input_entrada, 0)
                m.intercambiar(m.input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar 0 (misma columna)
                pos_num = m.buscar(m.input_entrada, num)
                pos_sig1 = m.buscar(m.input_entrada, sig1)
                pos_sig2 = m.buscar(m.input_entrada, sig2)

        elif sig1 != 0:
            pos_sig1 = m.buscar(m.input_entrada, sig1)
            # hasta que num y el siguiente no estén en el último cuadrante:
            while pos_sig1 not in ultimo_cuadrante and pos_num not in ultimo_cuadrante: # todo cambio or por and
                mover_fila_a_derecha()
                pos_cero = m.buscar(m.input_entrada, 0)
                m.intercambiar(m.input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
                mover_fila_a_izquierda()
                pos_cero = m.buscar(m.input_entrada, 0)
                m.intercambiar(m.input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar 0 (misma columna)
                pos_num = m.buscar(m.input_entrada, num)
                pos_sig1 = m.buscar(m.input_entrada, sig1)

        else:
            # hasta que num no esté en el ultimo_cuadrante
            while pos_num not in ultimo_cuadrante:
                mover_fila_a_derecha()
                pos_cero = m.buscar(m.input_entrada, 0)
                m.intercambiar(m.input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
                mover_fila_a_izquierda()
                pos_cero = m.buscar(m.input_entrada, 0)
                m.intercambiar(m.input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar 0 (misma columna)
                pos_num = m.buscar(m.input_entrada, num)


    cuadrar_esquina()  # coloco num y los 2 siguientes (si los hay) en el ultimo cuadrante y los ordeno
    input("fin cambiar esquina")
    pos_num = m.buscar(m.input_entrada, num)
    giros = 0
    print('Siguientes:', sig1, sig2)
    if sig2 != 0:
        pos_sig2 = m.buscar(m.input_entrada, sig2)
        pos_sig1 = m.buscar(m.input_entrada, sig1)
        print(f'  sig2 != 0  LN:290')
        while (pos_num != ultimo_cuadrante[0] and pos_sig1 != ultimo_cuadrante[3] and pos_sig2 != ultimo_cuadrante[1]) \
                and giros < 6: # todo cambio aquí
            # print(f'                                 --Entro en while de aqui 1\n'
            #       f'({pos_num != ultimo_cuadrante[2]} and {pos_sig1 != ultimo_cuadrante[3]}) and {giros != 5}')
            pos_cero = m.buscar(m.input_entrada, 0)
            m.intercambiar(m.input_entrada[pos_cero[0]][pos_cero[1] - 1])
            rotar4()
            giros += 1
            pos_num = m.buscar(m.input_entrada, num)
            pos_sig1 = m.buscar(m.input_entrada, sig1)
            pos_sig2 = m.buscar(m.input_entrada, sig2)

    elif sig1 != 0:
        pos_sig1 = m.buscar(m.input_entrada, sig1)
        print("      sig1 !=0 LN 307")
        # Mientras num no esté en (última fila) (ultima columna -1) y sig1 en esq inferior derecha y giros < 6
        while (pos_num != ultimo_cuadrante[2] and pos_sig1 != ultimo_cuadrante[3]) and giros < 6: # todo cambio aqui
            pos_cero = m.buscar(m.input_entrada, 0)
            if pos_cero[1] > 0:  # si 0 no está en la primera columna
                m.intercambiar(m.input_entrada[pos_cero[0]][pos_cero[1] - 1]) # lo muevo a la izquierda una posición
            else:
                input('   else en sig1 != 0')
                return None
            input(f'¿Aqui? giros:{giros}')
            rotar4()
            giros += 1
            pos_num = m.buscar(m.input_entrada, num)
            pos_sig1 = m.buscar(m.input_entrada, sig1)
            continue
        input("fuera del while")

    print("--giros:", giros)
    if giros < 6: # todo cambio aqui
        pos_cero = m.buscar(m.input_entrada, 0)
        m.intercambiar(m.input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
        pos_num = m.buscar(m.input_entrada, num)
        while pos_num != pos_esperada:
            mover_fila_a_derecha()
            pos_cero = m.buscar(m.input_entrada, 0)
            m.intercambiar(m.input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar fila (misma columna)
            mover_fila_a_izquierda()
            pos_cero = m.buscar(m.input_entrada, 0)
            m.intercambiar(m.input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
            pos_num = m.buscar(m.input_entrada, num)

        pos_cero = m.buscar(m.input_entrada, 0)
        m.intercambiar(m.input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar fila (misma columna)
    else:
        return None
