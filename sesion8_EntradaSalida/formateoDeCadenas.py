#  Formateo de cadenas: Consiste en mostrar variables dentro de una cadena

#  Forma antigua con 'place holders'
print("***************Forma antigua de formatear cadenas con 'place holders(%letra)'***********")
numero = 517
flotante = 1.55
texto = "quijote"
booleano = False

print("\n'-El número es %d(digit), el texto es %s(string) el flotante es %f(float), booleano es %r(boolean)' % "
      "(numero, texto, flotante, booleano))")
print("-El número es %d , el texto es %s, el flotante es %f, booleano es %r" % (numero, texto, flotante, booleano))

print("\n-Para mostrar un solo valor no hace falta poner paréntesis después de %'fuera de las comillas' EJ:")
print("'Valor flotante: %f' % flotante")
print("Valor flotante: %f" % flotante)

print("\n-Para modificar el nº de decimales en un float poner %.Xf siendo x el nº de decimales EJ:")
print("'Valor flotante: %.2f' % flotante")
print("Valor flotante: %.2f" % flotante)

# Forma para versiones 2.6 hasta 3.6 de python con función Format
print("\n\n***************Forma para versiones 2.6 hasta 3.6 de python con función .format(variables)***********")

print("\n'El número es {}, el texto es {}, el flotante es {}, booleano es {}'.format(numero, texto, flotante, "
      "booleano))")
print("El número es {}, el texto es {}, el flotante es {}, booleano es {}".format(numero, texto, flotante, booleano))

print("\n-Se puede hacer cambiando el lugar en que se muestra cada parámetro poniendo el {nº}")
print("'El flotante es {2}, el texto es {1}, el número es {0}, booleano es {3}'.format(numero, texto, flotante, "
      "booleano)")
print(
    "El flotante es {2}, el texto es {1}, el número es {0}, booleano es {3}".format(numero, texto, flotante, booleano))

print("\n-Se puede hacer poniendo un nombre a cada parámetro {nombre} y asignándolo dentro del paréntesis ("
      "nombre=texto)")
print("'El flotante es {fl}, el texto es {txt}, el número es {num}'.format(num=numero, txt=texto, fl=flotante)")
print("El flotante es {fl}, el texto es {txt}, el número es {num}".format(num=numero, txt=texto, fl=flotante))

# Forma para versiones desde 3.6 de python con fStrings
print(
    "\n\n***************Forma para versiones desde 3.6 de python con fStrings f'textos {parámetros} textos'***********")
print("-Simplemente se pone entre llaves el nombre real de el parámetro:\n")
print("f'El número es {numero}, flotante es {flotante}, texto es {texto}, booleano es {booleano}'")
print(f'El número es {numero}, flotante es {flotante}, texto es {texto}, booleano es {booleano}')

print("\n**Ojo permite usar métodos de cada clase de dato:")
print("f'el texto en mayúsculas es {texto.upper()}'")
print(f"el texto en mayúsculas es {texto.upper()}")

print("\n**Ojo también permite usar métodos directamente:")


def suma(a, b):
    return a + b


print("def suma(a, b):\n      return a + b")
print("f' el numero {numero} + 100 es = {suma(numero, 100)}")
print(f" el numero {numero} + 100 es = {suma(numero, 100)}")

# Modificación de tipo de parámetros
print("\n\n------------Modificación de tipo de parámetros----------------")
print("-Convertir a string con str(parámetro)")
num = 500
print(f"type(num) = {type(num)}")
numtxt = str(num)
print("numtxt = str(num)")

print(f"type(numtxt) = {type(numtxt)}")
print(f"print(numtxt): {numtxt}")


# *****************************************************************
print("\n\n+++++++++++++ USO DE __str__ (salidas informales)+++++++++++++++++++++++++")
print("\n-Ahora vamos a sobrecargar __str__ para modificar el formato de salida:")


class Juguete:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio):  # __init__ se encarga de hacer (Lo que queramos) al instanciar un objeto
        self.nombre = nombre
        self.precio = precio

    # Sobrecargamos el método __str__ para cambiar el formato que devuelve
    def __str__(self):
        return f'Mi nombre es {self.nombre} y mi precio {self.precio}'


j1 = Juguete("Potato", 10.56)
print("sólo para ver como se mostraría con __repr__ sin modificar. print(repr(j1)) =", repr(j1))
print("print(str(j1)) '__str__ esta sobrecargado en la clase' =", str(j1))

# *******************************************************************************
print("\n\n+++++++++++++ USO DE __repr__ (para salidas técnicas) +++++++++++++++++++++++++")
print("\n-Ahora vamos a sobrecargar __repr__ para modificar el formato de la representación:")


class Juguete2:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio):  # __init__ se encarga de hacer (Lo que queramos) al instanciar un objeto
        self.nombre = nombre
        self.precio = precio

    # Sobrecargamos el método __str__ para cambiar el formato que devuelve
    def __repr__(self):
        return f'j2({self.nombre},{self.precio})'


j2 = Juguete2("Pelota", 18.67)
print("print(repr(j2)) =", repr(j2))

print("\n\n!!!!!!!!!!!!!!!!!!!ATENCIÓN: sirven para lo mismo repr y str, pero cada cosa se usa dependiendo de "
      "si estamos en depuración(repr) o mostrando al usuaio(str)!!!!!!!!!!!!!!!!!!!!!!!")
print("-Si hemos sobreescrito __str__, al hacer repr se ejecutará el comportamiento standard de __repr__")
print("-Si hemos sobreescrito __repr__, se ejecutará el __repr__ aunque invoquemos __str__")
print("-Si hemos sobreescrito __str__ y __repr__, se ejecutará el que invoquemos")

#min 25
print("\n********************** Mas cosas con cadenas de texto ************************")
cadena = "en un lugar de la manchA"
print("--Vamos a trabajar con esta cadena de texto:", cadena)
print("\n-print(cadena.capitalize():", cadena.capitalize())
print("\n-print(cadena.title():", cadena.title())
print("\n-print(cadena.count('a'):", cadena.count('a'))
print("*Ojo no cuenta las 'A', por que no es lo mismo que 'a', para contarlas todas, las pasamos a minúsculas y "
      "luego contamos*")
print("\n-print(cadena.lower():", cadena.lower())
print("\n-print(cadena.lower().count('a')):", cadena.lower().count('a'))

numero = '5'
print("\n--Ahora vamos a trabajar con este número pasado como cadena (numero = '5'):", numero)
print("-print(numero.isdigit()):", numero.isdigit())
print("-print(cadena.isdigit()):", cadena.isdigit())

print("\n-print(numero.isalnum()) para saber si es alfanumérico:", numero.isalnum())
print("-print(cadena.isalnum()):", cadena.isalnum())


print("\n-print(numero.isalfa()) para saber si es alfabético:", numero.isalpha())
print("-print(cadena.isalfa()):", cadena.isalpha(), "\nPone False por que contiene espacios*")
print("-print('a'.isalfa()):", 'a'.isalpha())
print("*la función isalfa() solamente comprueba si es alfabético a-z A-Z*")

print("\n********** Otros métodos ***********")
print("-print(cadena.startswith('en')):", cadena.startswith('en'))
print("-print(cadena.startswith('  ')):", cadena.startswith('  '))
print("-print(cadena.endswith('manchA')):", cadena.endswith('manchA'))
print("-print(cadena.endswith('mancha')):", cadena.endswith('mancha'))








cadena = '          en un lugar de la manchA          '
print("\n*Modificamos la cadena así:\ncadena = '          en un lugar de la manchA          '")
print("-print(cadena.strip()):", cadena.strip())
print("*cadena.strip(), elimina los espacios sobrantes al principio y al final.*")
print("-print(cadena.lstrip()):", cadena.lstrip())
print("*cadena.lstrip(), elimina los espacios sobrantes al principio(izda), NO al final.*")
print("-print(cadena.rstrip()):", cadena.rstrip())
print("*cadena.rstrip(), elimina los espacios sobrantes al final(dcha).*")

print("\n****************** Función split() **********************")
print("-print(cadena.split()):", cadena.split(), "**Si no ponemos nada, separa por espacios")
print("-print(cadena.split('de')):", cadena.split('de'), "**En este caso divide cada vez que pone 'de'")

