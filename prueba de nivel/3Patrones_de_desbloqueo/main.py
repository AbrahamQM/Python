# Reto 3: Patrones de desbloqueo

import sys
import numpy as np

panel = np.array([
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
])
combinaciones = 0  # num de combinaciones
reg_secuencias = []  # Secuencias que ya se han usado


def posible(letra, destino, letras_usadas):
    pos_letra = np.where(panel == letra)
    pos_destino = np.where(panel == destino)

    def sin_saltar():
        for x in range(3):
            for y in range(3):
                if pos_destino == (x, y) and (
                        # horizontal
                        (x == int(pos_letra[0]) and y == int(pos_letra[1] - 1)) or
                        (x == int(pos_letra[0]) and y == int(pos_letra[1] + 1)) or
                        # Vertical
                        (x == int(pos_letra[0] - 1) and y == int(pos_letra[1])) or
                        (x == int(pos_letra[0] + 1) and y == int(pos_letra[1])) or
                        # diagonales
                        (x == int(pos_letra[0] + 1) and y == int(pos_letra[1] + 1)) or
                        (x == int(pos_letra[0] + 2) and y == int(pos_letra[1] + 1)) or
                        (x == int(pos_letra[0] + 1) and y == int(pos_letra[1] + 2)) or
                        (x == int(pos_letra[0] + 1) and y == int(pos_letra[1] - 1)) or
                        (x == int(pos_letra[0] + 2) and y == int(pos_letra[1] - 1)) or
                        (x == int(pos_letra[0] + 1) and y == int(pos_letra[1] - 2)) or
                        (x == int(pos_letra[0] - 1) and y == int(pos_letra[1] + 1)) or
                        (x == int(pos_letra[0] - 1) and y == int(pos_letra[1] + 2)) or
                        (x == int(pos_letra[0] - 1) and y == int(pos_letra[1] - 1)) or
                        (x == int(pos_letra[0] - 1) and y == int(pos_letra[1] - 2)) or
                        (x == int(pos_letra[0] - 2) and y == int(pos_letra[1] + 1)) or
                        (x == int(pos_letra[0] - 2) and y == int(pos_letra[1] - 1))
                ):
                    return True

    def buscar_intermedio():
        # vertical u horizontal
        if pos_letra[0] == pos_destino[0]:  # misma fila
            if pos_letra[1] < pos_destino[1]:  # Destino a la derecha de letra
                return panel[int(pos_letra[0])][int(pos_letra[1]) + 1]
            elif pos_letra[1] > pos_destino[1]:  # Destino a la izquierda de letra
                return panel[int(pos_letra[0])][int(pos_letra[1]) - 1]
        elif pos_letra[1] == pos_destino[1]:  # misma columna
            if pos_letra[0] < pos_destino[0]:  # Destino bajo letra
                return panel[int(pos_letra[0]) + 1][int(pos_letra[1])]
            elif pos_letra[0] > pos_destino[0]:  # Destino sobre  letra
                return panel[int(pos_letra[0]) - 1][int(pos_letra[1])]
        # diagonal
        else:
            return 'E'

    if letra == destino or destino in letras_usadas:
        return False

    # Devolvemos True en los destinos que están junto a la letra o en diagonal
    elif sin_saltar():
        return True

    # Casos en los que se haya usado saltar
    else:
        intermedio = str(buscar_intermedio())
        if intermedio in letras_usadas:
            return True
        else:
            return False


def buscar_siguientes(puntos_restantes, letra_actual, letras_usadas):
    global combinaciones
    if puntos_restantes > 0:

        for fila in panel:
            restantes_fila = puntos_restantes

            if restantes_fila > 0:
                reg_usadas_local = letras_usadas

                for letra in fila:

                    restantes_letra = restantes_fila
                    sig_letra = letra

                    if restantes_letra > 0:

                        if posible(letra_actual, sig_letra, reg_usadas_local):
                            reg_usadas_local.append(sig_letra)
                            restantes_letra -= 1

                            if restantes_letra > 0:
                                buscar_siguientes(restantes_letra, sig_letra, reg_usadas_local)
                                reg_usadas_local.remove(sig_letra)  # resetear reg_usadas_local

                            elif reg_usadas_local not in reg_secuencias:
                                globals()['reg_secuencias'].append(list(reg_usadas_local))
                                globals()['combinaciones'] += 1
                                reg_usadas_local.remove(letra)  # resetear reg_usadas_local

                    else:
                        restantes_fila -= 1
                        continue


def main():
    puntos = int(sys.argv[2])
    letra_comienzo = sys.argv[1].upper()
    global combinaciones
    global reg_secuencias
    # Analizamos el comienzo por cada una de las letras del panel
    for x in range(3):

        for y in range(3):
            letras_usadas = [letra_comienzo]
            letra_actual = panel[x][y]

            if posible(letra_comienzo, letra_actual, letras_usadas) and puntos > 1:
                # De las que son posibles, analizamos las siguientes posibilidades dentro de los movimientos que nos
                # pasan para cada combinación.
                puntos_restantes = puntos - 2  # Le resto 2 porque ya se han usado al llegar a aquí
                letras_usadas.append(letra_actual)

                if puntos_restantes > 0:
                    buscar_siguientes(puntos_restantes, letra_actual, letras_usadas)

                else:
                    reg_secuencias.append(list(letras_usadas))
                    combinaciones += 1
            else:
                pass

    if len(reg_secuencias) == combinaciones:
        print(combinaciones)
        return combinaciones 

    else:
        print("Error de numero de combinaciones")


if __name__ == '__main__':
    main()
