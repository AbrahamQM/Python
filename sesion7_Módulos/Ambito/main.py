# Un ámbito es al alcance de una función o variable en el contexto de nuestro programa
import pprint
letra = 'l'
numero = 4


def cosa():
    print("Hola")


print("\nTabla de símbolos globales pprint.pprint(globals()):")
pprint.pprint(globals())  # Imprime la (tabla de símbolos globales)

print("\n-Alteramos el contenido de una variable global con globals()['nombreDeVariable'] = 'x'")
print("letra =", letra)
print("globals()['letra'] = 'a'")
globals()['letra'] = 'a'
print("Ahora letra =", letra)

print("\n-Alteramos el contenido de una variable con una función: \ndef modificar():\n  globals()['letra'] = 'H'")
def modificar():
    globals()['letra'] = 'H'

modificar()
print("Ahora letra =", letra)

print("\n-Idem pero con otra sintaxis: \ndef modificar():\n global letra"
      "\n letra = 'D'")
def modificar():
    global letra
    letra = 'D'

modificar()
print("Ahora letra =", letra)

print("\n-Acceder a una variable o método de una clase con globals()[' ']")
print("class Hola():\n  def pepe(self):\n    print('Hola soy pepe')\nh = Hola()\nglobals()['h'].pepe()")
class Hola():
    def pepe(self):
        print("Hola soy pepe")

h = Hola()
globals()['h'].pepe()


print("\n--Tabla de símbolos locales pprint.pprint(locals()) 'para variables demtro de una funcion o clase':")

class Locales():
    def pepe(self, unParámetro):
        valor = 5
        estado = False
        print("Tabla de símbolos locales:")
        pprint.pprint(locals())  # Imprime la (tabla de símbolos locales)
h = Locales()
h.pepe("parámetro")
print("")
globals()['h'].pepe('parámetro accediendo desde globals()["h"].pepe ')


