# Reto 3: Patrones de desbloqueo
# Descripción del reto
# Este reto está inspirado en la funcionalidad de desbloqueo de dispositivos Android a través
# de las combinaciones disponibles en la pantalla de bloqueo conectando los puntos sin
# levantar el dedo de la pantalla
# Debes desarrollar una función capaz de encontrar el número de combinaciones posibles
# conectando los puntos disponibles.
# La imagen anterior muestra un patrón de 7 puntos conectados: (A -> B -> I -> E -> D -> G -> C)
# Objetivo:
# Deberás implementar una función que devuelva la cantidad de patrones posibles a partir de
# un primer punto dado, que tienen una longitud determinada.
# Los puntos a conectar serían:
# | A | B | C |
# | D | E | F |
# | G | H | I |
# La función contará con un primer parámetro de tipo caracter correspondiente al punto de la
# cuadrícula (A, B, C, D, E, F, G, H o I).
# La función contará con un segundo parámetro de tipo numérico correspondiente al número
# de puntos que debe tener cada patrón.
# Por ejemplo:
# Por ejemplo, pasar los parámetros “C" y 2, debería devolver el número de patrones que
# comienzan en 'C' y que tienen 2 conexión de dos puntos. El valor de retorno en este caso
# sería 5, porque hay 5 patrones posibles:
# (C -> B), (C -> D), (C -> E), (C -> F) y (C -> H).
# No debe devolver los patrones en sí, solo el número de patrones posibles.
# Reglas
# ● En un patrón, los puntos/puntos no se pueden repetir: solo se pueden usar una vez,
# como máximo.
# ● En un patrón, dos puntos/puntos posteriores cualesquiera solo se pueden conectar
# con líneas rectas directas de cualquiera de estas formas:
# ○ Horizontalmente: como (A -> B).
# ○ Verticalmente: como (D -> G).
# ○ Diagonalmente: como (I -> E), así como (B -> I).
# ● Pasando por encima de un punto entre ellos que ya ha sido 'usado': como (G -> C)
# pasando por encima de E, en la imagen del patrón de ejemplo.
# ○ Esta es la regla más complicada. Normalmente, no podría conectar G con C,
# porque E está entre ellos, sin embargo, cuando E ya se ha utilizado como
# parte del patrón que está rastreando, puede conectar G con C pasando por
# E, porque E se ignora, al haber sido usado.
import sys
import numpy as np

panel = np.array([
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
])

global movimientos
movimientos = 0


def posible(letra, destino, usados):
    pos_letra = np.where(panel == letra)
    pos_destino = np.where(panel == destino)
    if (pos_letra == pos_destino) or (destino in usados):
        # print(f'FALSE, pos_letra:{pos_letra}, pos_destino:{pos_destino}')
        return False
    # todo Casos en los que se haya usado saltar

    # Devolvemos True en los destinos que están junto a la letra o en diagonal
    else:
        for x in range(3):
            for y in range(3):
                if pos_destino == (x, y) and (
                        # horizontal
                        (x == int(pos_letra[0]) and y == int(pos_letra[1]-1)) or
                        (x == int(pos_letra[0]) and y == int(pos_letra[1]+1)) or
                        # Vertical
                        (x == int(pos_letra[0]-1) and y == int(pos_letra[1])) or
                        (x == int(pos_letra[0]+1) and y == int(pos_letra[1])) or
                        # diagonales
                        (x == int(pos_letra[0]+1) and y == int(pos_letra[1]+1)) or
                        (x == int(pos_letra[0]+2) and y == int(pos_letra[1]+1)) or
                        (x == int(pos_letra[0]+1) and y == int(pos_letra[1]+2)) or
                        (x == int(pos_letra[0]+1) and y == int(pos_letra[1]-1)) or
                        (x == int(pos_letra[0]+2) and y == int(pos_letra[1]-1)) or
                        (x == int(pos_letra[0]+1) and y == int(pos_letra[1]-2)) or
                        (x == int(pos_letra[0]-1) and y == int(pos_letra[1]+1)) or
                        (x == int(pos_letra[0]-1) and y == int(pos_letra[1]+2)) or
                        (x == int(pos_letra[0]-1) and y == int(pos_letra[1]-1)) or
                        (x == int(pos_letra[0]-1) and y == int(pos_letra[1]-2)) or
                        (x == int(pos_letra[0]-2) and y == int(pos_letra[1]+1)) or
                        (x == int(pos_letra[0]-2) and y == int(pos_letra[1]-1))
                ):
                    return True



def main(**argv):
    pos_comienzo = np.where(panel == sys.argv[1].upper())
    puntos = int(sys.argv[2])
    letra_comienzo = sys.argv[1].upper()
    global movimientos
    usados = [letra_comienzo]

    for opciones in range(puntos): # todo afinar lo de los puntos

        for x in range(3):
            for y in range(3):
                letra = panel[x][y]
                if posible(letra_comienzo, letra, usados):
                    print(f'{letra_comienzo}->{letra}')
                    usados.append(letra)
                    movimientos += 1


            # if panel[pos_comienzo[0]][pos_comienzo[1]] not in usados: # si no está en la lista de usados
            # if letra != letra_comienzo and letra not in usados:
            #     print(f'{letra_comienzo}->{letra}')
            #     usados.append(letra)
            #     movimientos += 1

    print("Fin del código", usados, movimientos)




if __name__ == '__main__':
    main()
