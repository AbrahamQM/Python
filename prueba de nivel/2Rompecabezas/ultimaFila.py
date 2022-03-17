import main as m


def ultima_fila(num):
    res_esperado = m.res(m.input_entrada)
    pos_esperada = m.buscar(m.res(m.input_entrada), num)
    pos_num = m.buscar(m.input_entrada, num)
    ultimo_cuadrante = [(len(m.input_entrada[0]) - 2, len(m.input_entrada[1]) - 2),
                        (len(m.input_entrada[0]) - 2, len(m.input_entrada[1]) - 1),
                        (len(m.input_entrada[0]) - 1, len(m.input_entrada[1]) - 2),
                        (len(m.input_entrada[0]) - 1, len(m.input_entrada[1]) - 1)]

    if num != int(res_esperado.max()):
        print("hay un número más")
        sig1 = num + 1
        pos_sig1 = m.buscar(m.input_entrada, sig1)
        if sig1 != int(res_esperado.max()):
            sig2 = num + 2
            pos_sig2 = m.buscar(m.input_entrada, sig2)
            print("hay dos números más")
        else:
            sig2 = 0
    else:
        sig1 = 0

    print("Entrada:\n", m.input_entrada)

    def mover_fila_a_derecha():
        print("*******Mover_fila_a_derecha()********")
        pos_cero = m.buscar(m.input_entrada, 0)
        while pos_cero[1] != 0:
            m.intercambiar(m.input_entrada[pos_cero[0]][pos_cero[1] - 1])
            # print(input_entrada)
            pos_cero = m.buscar(m.input_entrada, 0)
        print("///Fin mover_fila_a_derecha")
    def mover_fila_a_izquierda():
        print("*******Mover_fila_a_izquierda()********")
        pos_cero = m.buscar(m.input_entrada, 0)
        while pos_cero[1] != len(m.input_entrada[1])-1:
            m.intercambiar(m.input_entrada[pos_cero[0]][pos_cero[1] + 1])
            pos_cero = m.buscar(m.input_entrada, 0)
        print("///Fin mover_fila_a_izquierda")

    def rotar4():
        print("             000000000     ROTAR4")
        pos_cero = m.buscar(m.input_entrada, 0)
        m.intercambiar(m.input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
        m.intercambiar(m.input_entrada[pos_cero[0] - 1][pos_cero[1] + 1])  # Mover a derecha
        m.intercambiar(m.input_entrada[pos_cero[0]][pos_cero[1] + 1])  # Bajar fila (misma columna)
        m.intercambiar(m.input_entrada[pos_cero[0]][pos_cero[1]])  # Vuelve a pos inicial

        print("                                 -----FIn de rotar4------")


    # ROTAMOS LAS DOS ÚLTIMAS FILAS hasta que num, sig1 y sig2(en caso de haberlo) estén en la esquina inferior derecha
    def cuadrar_esquina():
        print("                Dentro de cuadrar_esquina")
        pos_num = m.buscar(m.input_entrada, num)
        if sig2 != 0:
            pos_sig1 = m.buscar(m.input_entrada, sig1)
            pos_sig2 = m.buscar(m.input_entrada, sig2)
            # hasta que num y los 2 siguientes no estén en el último cuadrante:
            while pos_sig2 not in ultimo_cuadrante or pos_sig1 not in ultimo_cuadrante \
                    or pos_num not in ultimo_cuadrante:
                print("                                       Estoy en el while con 2 numeros mas")
                mover_fila_a_derecha()
                pos_cero = m.buscar(m.input_entrada, 0)
                m.intercambiar(m.input_entrada[pos_cero[0]-1][pos_cero[1]]) # Subir fila (misma columna)
                mover_fila_a_izquierda()
                pos_cero = m.buscar(m.input_entrada, 0)
                m.intercambiar(m.input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar 0 (misma columna)
                pos_num = m.buscar(m.input_entrada, num)
                pos_sig1 = m.buscar(m.input_entrada, sig1)
                pos_sig2 = m.buscar(m.input_entrada, sig2)

        elif sig1 != 0:
            pos_sig1 = m.buscar(m.input_entrada, sig1)
            # hasta que num y el siguiente no estén en el último cuadrante:
            while pos_sig1 not in ultimo_cuadrante or pos_num not in ultimo_cuadrante:
                mover_fila_a_derecha()
                pos_cero = m.buscar(m.input_entrada, 0)
                m.intercambiar(m.input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
                mover_fila_a_izquierda()
                pos_cero = m.buscar(m.input_entrada, 0)
                m.intercambiar(m.input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar 0 (misma columna)
                pos_num = m.buscar(m.input_entrada, num)
                pos_sig1 = m.buscar(m.input_entrada, sig1)
                print("                                       Estoy en el while con 1 numero mas")
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
                print("                                       Estoy en el while sin mas numeros ")

        print("5555555555555555555555    FIN DE cuadrar_esquina, pos_num:", pos_num)


    cuadrar_esquina() # coloco num y los 2 siguientes si los hay en el ultimo cuadrante y los ordeno

    pos_num = m.buscar(m.input_entrada, num)
    giros = 0
    print('Siguientes:', sig1, sig2)
    if sig2 != 0:
        pos_sig2 = m.buscar(m.input_entrada, sig2)
        pos_sig1 = m.buscar(m.input_entrada, sig1)
        print(f'                    ************************ aqui 1  ')
        while (pos_num != ultimo_cuadrante[0] and pos_sig1 != ultimo_cuadrante[3] and pos_sig2 != ultimo_cuadrante[1]) \
                and giros != 5:
            print(f'                                 --Entro en while de aqui 1\n'
                  f'({pos_num != ultimo_cuadrante[2]} and {pos_sig1 != ultimo_cuadrante[3]}) and {giros != 5}')
            pos_cero = m.buscar(m.input_entrada, 0)
            m.intercambiar(m.input_entrada[pos_cero[0]][pos_cero[1]-1])
            rotar4()
            giros += 1
            pos_num = m.buscar(m.input_entrada, num)
            pos_sig1 = m.buscar(m.input_entrada, sig1)
            pos_sig2 = m.buscar(m.input_entrada, sig2)
            print(f'                                 ++salgo en while de aqui 1\n'
                  f'({pos_num != ultimo_cuadrante[2]} and {pos_sig1 != ultimo_cuadrante[3]}) and {giros != 5}')

    elif sig1 != 0:
        pos_sig1 = m.buscar(m.input_entrada, sig1)
        print("                            ************************aqui 2")
        while (pos_num != ultimo_cuadrante[2] and pos_sig1 != ultimo_cuadrante[3]) and giros != 5:
            pos_cero = m.buscar(m.input_entrada, 0)
            m.intercambiar(m.input_entrada[pos_cero[0]][pos_cero[1] - 1])
            rotar4()
            giros += 1
            pos_num = m.buscar(m.input_entrada, num)
            pos_sig1 = m.buscar(m.input_entrada, sig1)


    print(giros)
    if giros != 5:
        pos_cero = m.buscar(m.input_entrada, 0)
        m.intercambiar(m.input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)
        pos_num = m.buscar(m.input_entrada, num)
        while pos_num != pos_esperada:#         todo por aquí
            mover_fila_a_derecha()
            pos_cero = m.buscar(m.input_entrada, 0)
            m.intercambiar(m.input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar fila (misma columna)
            mover_fila_a_izquierda()
            pos_cero = m.buscar(m.input_entrada, 0)
            m.intercambiar(m.input_entrada[pos_cero[0] - 1][pos_cero[1]])  # Subir fila (misma columna)

            pos_num = m.buscar(m.input_entrada, num)
            input(f'STOP, pos_num:{pos_num}, pos_esperada:{pos_esperada}')
        pos_cero = m.buscar(m.input_entrada, 0)
        m.intercambiar(m.input_entrada[pos_cero[0] + 1][pos_cero[1]])  # bajar fila (misma columna)
    else:
        return None


