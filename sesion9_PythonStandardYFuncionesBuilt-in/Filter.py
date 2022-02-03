numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("************************************** FUNCIÓN FILTER *****************************************")
print("--La función filter(), discrimina según el método que hayamos definido "
      "y,\ndevuelve otra lista con los valores que obtengan True al aplicar nuestro método o lambda")
print("***********************************************************************************************")
print("\nSe ejecuta:\nfilter(FUNCION, lista)")
print("Esa función debemos implementarla previamente o crear una lambda en lugar de la palabra FUNCION")


# La función debe devolver true o false(Si devuelve True, filter mantendrá el número, si devuelve False, lo eliminará
# de la lista
def miFuncion(x):
    if x % 2 == 0:
        return True  # Devolverá True sólo los números que sean pares


resultado = filter(miFuncion, numeros)  # por cada elemento de la lista, se va a ejecutar miFuncion(elementoDeLista)
print(f'-Resultado de print(list(resultado)): {list(resultado)}')

print("\n-Usando una lambda: resultado = filter(lambda x: x % 2 == 0, numeros)")
resultado = filter(lambda x: x % 2 == 0, numeros)
print(f'Resultado de print(list(resultado)): {list(resultado)}')


nombres = ['Lucas', 'Pepito', 'Abraham', 'Pepe', 'Pelota']


print("\n**Otro ejemplo de función para filter: \n-función que devuelve los nombres que comienzan con 'Pe'"
      "de la lista:", nombres)


def miFuncion(x):
    if str(x).startswith('Pe'):
        return True


resultado = filter(miFuncion, nombres)
print(f'Resultado: {list(resultado)}')

print("\n**Idem pero con lambda: filter(lambda x: str(x).startswith('Pe'), nombres)")
print(list(filter(lambda x: str(x).startswith('Pe'), nombres)))

