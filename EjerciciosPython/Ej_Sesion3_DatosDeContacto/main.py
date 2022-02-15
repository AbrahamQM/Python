# Para este ejercicio tenéis que crear un archivo main.py y dentro tienes que crear variables que representen los
# siguientes datos de un contacto:
#
#
# - Nombre
# - Apellidos
# - Edad
# - Email
# - Teléfono
# - Casado (verdadero o falso)
# - Con Hijos (verdadero o falso)
# - Lista de amigos
# - Películas vistas (diccionario con clave y valor. El valor será el título de la película)
#
# Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print().



def booleanos():
    global casado
    global hijos
    condenado = input('¿Está Casado? S/N: ')
    if condenado.lower() == 's':
        casado = True
    else:
        casado = False
    hijo = input('¿Tiene Hijos? S/N: ')
    if hijo.lower() == 's':
        hijos = True
    else:
        hijos = False


def pelis():
    global peliculas
    peliculas = {}
    i = 1
    mas = True
    while mas:

        añadir = input("¿Desea añadir película vista? S/N: ")
        if añadir != 's' and añadir != 'S':
            mas = False
        else:
            peliculas[i] = input('Nombre de la película: ')
            i += 1


def amigos():
    global friends
    friends = []
    mas = True
    while mas:
        añadir = input("¿Desea añadir un amigo? S/N: ")
        if añadir != 's' and añadir != 'S':
            mas = False
        else:
            print("Introduzca nombre: ")
            friends.append(input())


def main():
    nombre = input('Nombre: ')
    apellidos = input("Apellidos: ")
    edad = input('Edad: ')
    email = input('Email: ')
    telefono = input('Teléfono: ')
    booleanos()
    pelis()
    amigos()
    print(f'\n------Usuario------\n**Nombre:{nombre}\n*Apellidos:{apellidos}\n*Edad:{edad}  *Email:{email}  *Teléfono:{telefono}\n'
          f'*Está casado: {casado}  *Tiene hijos: {hijos}\n*Películas vistas:')

    for pelicula in peliculas:
        print(f'-{pelicula}: {peliculas[pelicula]}')

    print("*Amigos:", friends)
    for amigo in friends:
        print(f'-{amigo}')


if __name__ == '__main__':
    main()

