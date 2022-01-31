import operaciones as op
# 'as op' Hace que podamos usar all lo que hay en el módulo operaciones
# usando solo op.método en lugar de opareciones.método

def main():
    print("resultado de print(op.comoMeLlamo()):", op.comoMeLlamo())
    print("resultado de print(op.__name__):", op.__name__)
    sum = op.suma(2, 2)
    res = op.resta(8, 4)
    print("suma(2,2):", sum, "\nresta(8,4):", res)

    # EJEMPLO DE UN MÓDULO QUE INCLUYE UNA CLASE CON SUS MÉTODOS
    # Creamos una instancia de la clase Operador y usamos el método multiplicación
    print("\n**EJEMPLO DE UN MÓDULO QUE INCLUYE UNA CLASE CON SUS MÉTODOS")
    o = op.Operador.multiplicacion(None, 4, 2)
    print("Resultado de op.Operador.multiplicacion(None, 4, 2):", o)


if __name__ == "__main__":
    main()