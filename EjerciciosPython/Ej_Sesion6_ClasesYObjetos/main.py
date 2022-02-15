# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
#
# - Color
# - Ruedas
# - Puertas
#
# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
#
# - Velocidad
# - Cilindrada
#
# Por último, crearéis un objeto de la clase Coche y lo mostraréis por consola.
class Vehiculo:
    print("***Nuevo objeto de la clase Vehículo***")
    color = input("Introduzca color:\n")
    ruedas = int(input("Introduzca nº de ruedas:\n"))
    puertas = int(input("Introduzca nº de puertas:\n"))


class Coche(Vehiculo):
    print("***Nuevo objeto de la clase Coche que hereda de Vehículo***")
    velocidad = int(input("Introduzca velocidad:\n"))
    cilindrada = int(input("Introduzca cilindrada:\n"))


def main():
    c = Coche()
    print(f'Vehículo de la clase:{type(c)}\n-Color:{c.color}\n-Nº ruedas:{c.ruedas}\n-Nº puertas:{c.puertas}'
          f'\n-Velocidad:{c.velocidad}\n-Cilindrada:{c.cilindrada}')


if __name__ == '__main__':
    main()
