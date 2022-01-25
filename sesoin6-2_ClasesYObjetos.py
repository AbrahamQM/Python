#  Seguimos en el minuto 29

print("Crear un constructor de una clase, se hace utilizando '__init__'\n")


class Juguete():
    color = None

    def __init__(self):  # __init__ se encarga de hacer (Lo que queramos) al instanciar un objeto
        print("...Estoy en el constructor de Juguete")
        self.color = "verde"


j = Juguete()

print("(Fuera del constructor) El juguete es de color:", j.color)

# Ejemplo del constructor, con un parámetro 'nombre
print("\n--Ejemplo del constructor, con un parámetro 'nombre'\n")


class Dino(Juguete):
    nombre = None

    def __init__(self, nombre):
        print("...Estoy en el constructor de Dino, con nombre", nombre)
        self.nombre = nombre


print("Creamos un objeto de la clase Dino con el parámetro 'T-Rex'")
d = Dino("T-Rex")

# ************************ Destructores ************************
print("\n\n************************ Destructores ************************")
print("--El destructor se invoca automáticamente cuando ya no hay más referencias a esa clase\n")


class Cosa():
    def __init__(self):  # __init__ se encarga de hacer (Lo que queramos) al instanciar un objeto
        print("...Estoy en el constructor de la clase:", self.__class__)

    def __del__(self):  # __del__ se encarga de hacer (Lo que queramos) al destruirse un objeto
        print("...Estoy en el destructor de la clase:", self.__class__)


c = Cosa()
print("\nCódigo para comprobar que aún no se ha ejecutado el destructor")
print("\nObligamos a destruir el objeto de la clase Cosa con del(nombreObjeto): del(c)")
del (c)

# ***************Hacer que el constructor instancie al constructor de la clase padre **************
print("\n*************Hacer que el constructor instancie al constructor de la clase padre **************")
print("-Método menos habitual: ClasePadre.__init__(self)")


class Coche(Juguete):
    nombre = None

    def __init__(self, nombre):
        Juguete.__init__(self)  # ClasePadre.__init__(self)
        print("...Estoy en el constructor de Coche, con nombre", nombre)
        self.nombre = nombre


bmw = Coche("bmw")

print("\n-Método más habitual: super().__init__()")


class Moto(Juguete):
    nombre = None

    def __init__(self, nombre):
        super().__init__()  # super().__init__()
        print("...Estoy en el constructor de Moto, con nombre", nombre)
        self.nombre = nombre


suki = Coche("suzuki")

# ****************************** CLASES ABSTRACTAS *****************************
# Para que sean abstractas debemos importar: from abc import ABC, abstractmethod
# Igual que en Java, no se puede instanciar una clase abstracta

print("\n\n********************* CLASES ABSTRACTAS ***********************")
print("--Para que sean abstractas debemos importar: from abc import ABC, abstractmethod\nIgual que en Java,"
      " no se puede instanciar una clase abstracta")
print("--La clase abstracta que definamos, debe heredar de 'ABC' asi: class Animal(ABC): ")
print("--Los métodos deben tener la anotacion '@abstractmethod'")
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod  # También añadir la anotacion @abstractmethod
    def sonido(self):
        pass  # Lo dejamos sin el código, para que se implementen los métodos en la clase que lo implemente


# Clase que implementa la clase abstracta Animal y sus métodos
class Perro(Animal):
    def sonido(self):
        print("Guau guau")


class Gato(Animal):
    def sonido(self):
        print("Miau Miau")


p = Perro()
print("\n-Creamos un objeto de la clase 'Perro', que implementa la clase 'Animal' y su método 'sonido'")
print("p.sonido:")
p.sonido()

g = Gato()
print("\n-Creamos un objeto de la clase 'Gato', que implementa la clase 'Animal' y su método 'sonido'")
print("g.sonido:")
g.sonido()


# ******************* Composición (Has a)***********************
print("\n\n******************* Composición (Has a) ***********************")
# La composición dice que una clase esta compuesta de otras clases
print("La composición dice que una clase esta compuesta de otras clases, y no hereda funciones")
class Motor:
    tipo = "Diesel"
    def cambiarTipo(self, tipo):
        self.tipo = tipo

class Ventanillas:
    cantidad = 120

class Ruedas:
    cantidad = 16

class Fuselaje:
    Ventanillas = Ventanillas()
    Ruedas = Ruedas()


class Avion:
    motor = Motor()
    fuselaje = Fuselaje()

boeing = Avion()
print("Avión con motor:", boeing.motor.tipo)
print("Avión con Fuselaje compuesto de :", boeing.fuselaje.Ventanillas.cantidad,
      "ventanillas y,", boeing.fuselaje.Ruedas.cantidad, "Ruedas")
print("-Cambiamos el tipo de motor con: boeing.motor.cambiarTipo('Queroseno')")
boeing.motor.cambiarTipo("Queroseno")
print("Ahora el avión tiene motor de:", boeing.motor.tipo)