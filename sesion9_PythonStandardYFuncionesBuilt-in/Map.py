print("**************************************** FUNCIÓN MAP ********************************************************")
print("--La función map, aplica indiscriminadamente el método que hayamos definido a cada elemento de la lista y,"
      "\n devuelve otra lista con el resultado de las operaciones")
print("*************************************************************************************************************")
print("\nSe ejecuta:\nmap(FUNCION, lista)")
print("Esa función debemos implementarla previamente o crear una lambda en lugar de la palabra FUNCION")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\n*Ejemplo función que devuelve el cuadrado de cada número de la lista:", numeros)
print("def cuadrado(x):\n  return x * x\nresultado = map(cuadrado, numeros)")

def cuadrado(x):
    return x * x


resultado = map(cuadrado, numeros)
print(f'Resultado: {list(resultado)}')

print("\n*Ejemplo con lambda map(lambda x: x * x, numeros):")
resultado = map(lambda x: x * x, numeros)
print(f'Resultado: {list(resultado)}')




