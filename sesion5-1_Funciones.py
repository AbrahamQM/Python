# Funciones
# def nombreFuncion(parámetros):
#   codigo

# Siempre debe estar la función antes de poder usarla o invocarla, o da error
import kwargs as kwargs

print("\n-Ejemplo de función básica que saluda")
def saludo():
    print("hola")


print("Antes de saludar")
saludo()
print("Despues de saludar")

print("\n-Ejemplo2 de función básica que imprime números 1-5")
def ejemplo2():
    for i in range(1, 6):
        print(i)
    # saludo() #También se puede llamar a otras funciones
ejemplo2()

# Ejemplo con parámetros:
print("\n-Ejemplo de función con parámetros(nombre)")
def miFuncion(nombre):
    print("Hola", nombre)

miFuncion("pepe")

# Ejemplo suma con parámetros
print("\n-Ejemplo de función suma(nº1, nº2)")

def suma(numero1, numero2):
    print("Resultado:", numero1 + numero2)

suma(5, 2)

# funciones dentro de funciones.
# Sólo se pueden invocar funciones que están dentro de otras dentro de la primera, no desde fuera.
print("\n-Ejemplo de función con funciones dentro de estas.")
def matematicas(a, b):
    def resta(a, b):
        print(a - b)

    def sum(a, b):
        print(a - b)

    sum(a, b)
    resta(a, b)

matematicas(1, 9)

# ***************** VARIABLES DE FUNCIONES ************************
# Variables dentro de una función, sólo se pueden usar dentro de la función
# No podemos acceder desde fuera.
# SI LA VARIABLE ESTÁ FUERA DE LA FUNCIÓN, SI PODREMOS ACCEDER DESDE DENTRO
print("\n-Ejemplo de variables externas e internas, variable local y global con el mismo nombre"
      "para comprobar cual se usa en cada caso")
hoyEs = "martes"
def func():
    hoyEs = "jueves"  # Una variable local que tapa a la variable global, se llama shadowing
    print("hoyEs DENTRO de mi función:", hoyEs)
func()
print("hoyEs FUERA de mi función:", hoyEs)


print("\n-Ejemplo2 de variables externas e internas, acceso a variables globales.")
def func():
    print("hoyEs DENTRO de mi función:", hoyEs)

func()

# Para los casos de shadowing, en caso de querer acceder a la variable global usamos la palabra 'global' así:
print("\n-Ejemplo3 Shadowing, acceso a variables globales con la palabra 'global'.")
def func():
    global hoyEs  # Hace que en lugar de crear una variable local, se trabaje la global
    hoyEs = "jueves"
    print("hoyEs DENTRO de mi función:", hoyEs)

func()
print("hoyEs FUERA de mi función:", hoyEs)

# ************* Parámetros Opcionales
# Podemos definir una función definiendo un parámetro por defecto asi:
print("\n--parámetros opcionales:")
print("-Ejemplo 1 con un parámetro opcional 'nombre'")
def miFuncion(nombre="pepe(parámetro por defecto)"):
    print("hola", nombre)
miFuncion() # En este caso se usará el parámetro por defecto
miFuncion("Lucas(parámetro que le pasamos al invocar la función)") #En este, se usará el parámetro que le pasamos

print("\n-Ejemplo 2, con 3 parámetros opcionales suma(a=1, b=2, c=3)")
def suma(a = 1, b = 2, c = 3):
    print(a + b + c)
suma()
suma(5, 9, 1)

print("!!!OJO¡¡¡, LOS PARÁMETROS OPCIONALES PUEDEN SER TODOS O LOS ÚLTIMOS, no se puede así:def suma(a = 0, b):")
print("Lo que si podemos hacer es invocar la funcion pasándole solo alguno/os de los parámetros"
      "\nLos leerá o colocará sustituyendo LOS PRIMEROS parámetros")
print("Por ejemplo así: suma(5, 1)")
suma(5, 1)

print("También podemos decidir cual es el parámetro que queremos pasarle indicando el nombre al invocarla asi:"
      "\nsuma(c=9, b=1), con la intención de pasarle los parámetros que queramos en el orden que queramos")
suma(c=9, b= 1)

#   ********** Parámetros variables ***************
# Podemos declarar una función sin especificar los parámetros de forma que puede haber 0, 4, 500 o lo que necesitemos
# Python va a crear una tupla con esos parámetros.
# Se implementa así: def función(*args)
print("\n**************Funciones con parámetros variables.")
print("*Se implementan así: def función(*args): "
      "\n(python crea una tupla con los parámetros)\n-Ejemplo:")

def suma(*args):
    print("Parámetros(tupla):", args)
    total = 0
    for parametro in args:
        total += parametro
    print("Resultado:", total)

suma(1, 2, 8, 17, 0, -9, 6, 0, 0, 0)

print("\n*Otra forma de implementarlo (parámetros con nombre): def función(**kwargs):")
print("(python crea un diccionario con 'clave': 'valor')\n-Ejemplo:")

def esBonito(**kwargs):
    print("Parámetros(diccionario):", kwargs)
    if kwargs['bonito'] == 'bonito':
        print( kwargs['nombre'], "tu coche", kwargs['coche'], "es bonito" )

esBonito(nombre = "pepe", bonito = "bonito", coche ="BMW X5")
# Aunque la implementación de este ejemplo no permitiría ejecutarlo sin argumentos (porque necesita que existan
# esos argumentos para poder funcionar, se podría hacer un código que no necesite esos argumentos asi:
def esBonito(**kwargs):
    print("Parámetros(diccionario):", kwargs)

print("\n**Ejemplo para que se vea que los argumentos son opcionales")
print("-Invocamos sin argumentos:")
esBonito()
print("-Invocamos com argumentos:")
esBonito(nombre = "pepe", bonito = "bonito", coche ="BMW X5")

