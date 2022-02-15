# Por último, tendréis que crear otro archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella,
# lo guardaréis en un archivo y luego lo cargamos.
import pickle


class Vehiculo:
    tipo = input("*Tipo de vehiculo:\n")
    capacidad = input("*Nº de pasajeros:\n")

    def getTipo(self):
        return self.tipo

    def getCapacidad(self):
        return self.capacidad


def main():
    v = Vehiculo()
    print("****Abriendo objeto.bin para almacenar datos ...")
    file = open('venv/objeto.bin', 'wb')
    print("\n**Guardando datos en objeto.bin ...")
    pickle.dump(v, file)
    file.close()
    print("\n**Cerrando objeto.bin ...")

    print("\n****Abriendo objeto.bin para leer datos ...")
    file = open('venv/objeto.bin', 'rb')
    print("\n**Cargando datos en memoria ...")
    datos = pickle.load(file)
    print("\n**Objeto cargado:")
    print(f'-Tipo de objeto: {type(datos)}\n-Accedemos el método getTipo(): {datos.getTipo()} '
          f'\n-Accedemos a una variable (capacidad): {datos.capacidad}')
    file.close()

if __name__ == '__main__':
    main()

