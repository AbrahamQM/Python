# necesitamos importar el paquete
from functools import reduce

print("************************************* FUNCIÓN REDUCE ********************************************************")
print("--La función reduce, va a ejecutar reiterativamente una función sobre la lista que le pasemos,\nhasta que quede un "
      "único elemento que nos va a devolver")
print("*************************************************************************************************************")
print("\nSe ejecuta:\nreduce(FUNCION, lista)")
print("Esa función debemos implementarla previamente o crear una lambda en lugar de la palabra FUNCION")

numeros = [1, 2, 3, 4, 5]
print("\n*Ejemplo usando una función que sume los valores uno por uno de la lista:", numeros)
print("def suma(a, b):\n  print(f' a = {a},   b = {b}')\n  return a + b\nresultado = reduce(suma, numeros)\nprint(resultado)")

print("-He puesto un print dentro de la función para que se vea como funciona:\n")


def suma(a, b):
      print(f' a = {a},   b = {b}')
      return a + b


resultado = reduce(suma, numeros)

print(f'-Resultado: {resultado}')

print("\n*Idem usando una lambda: \nresultado = reduce(lambda a, b: a + b, numeros) ")
resultado = reduce(lambda a, b: a + b, numeros)
print(f'-Resultado: {resultado}')



