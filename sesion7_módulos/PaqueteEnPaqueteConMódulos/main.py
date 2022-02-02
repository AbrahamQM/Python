import sumador.sumar as s
import restador.restar as r

# Otra forma de importar ambos módulos a la vez, sería:
# from sesion7_Módulos.PaqueteEnPaqueteConMódulos import restador, sumador

def main():
    # resta = r.resta(5, 3)
    # suma = s.suma(5, 3)

    suma = s.suma(5, 3)
    resta = r.resta(5, 3)
    help(s.suma) # Muestra los comentarios que hemos creado o que ya existían sobre este método
    print("\nsumador.suma(5, 3):", suma)
    print("restador.resta(5, 3):", resta)


if __name__ == '__main__':
    main()
