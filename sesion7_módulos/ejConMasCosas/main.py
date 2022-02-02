import sys
import operaciones
import pprint  # para mostrar resultados de forma mas "visible"

def main():
    print(operaciones.PI)  # Acceso a atributos del modulo operaciones
    print("\nLista de ubicaciones en las que el intérprete busca los paquetes para hacer 'import':")
    pprint.pprint(sys.path)  # sys.path: devuelve una lista de ubicaciones en las que el intérprete
    # busca los paquetes para hacer 'import'
    print("\n-operaciones.Operador.multiplicacion( None, 5, 5):", operaciones.Operador.multiplicacion( None, 5, 5))

if __name__ == "__main__":
    main()