# Para devolver un resultado en python se hace igual que en java, pero no hay que ponerlo en la declaración
print("Ejemplo básico de función con retorno")
def suma(a, b): # no se pone int, ni void, ni String, ...
    return a + b

print(suma(5,2))

print("Otro ejemplo devuelve varios resultados de forma simultanea, python crea una tupla con el resultado")
def operaciones(a, b):
    return a + b, a - b, a * b, a / b

print("\nResultado de operaciones sin tratar:", operaciones(5, 2))
suma, resta, multi, div = operaciones(5, 2)
print("\nResultado asignando los valores a variables(se asignan en el mismo orden):")
print("suma, resta, multi, div = operaciones(5, 2):")
print(suma)
print(resta)
print(multi)
print(div)

print ("\n*Para ignorar alguno de los resultados se suele usar '_' en lugar de un nombre de variable")
print("suma, _, _, _ = operaciones(5, 2)\nprint(suma)")
print("*Otra forma de hacerlo:\nsuma = operaciones(5, 2) \n print(suma[0])")


# Función con operador ternario
# Python: final = ['final'] if 'final' in kwargs else 0
# Java:   final = kwargs["final"] ? kwargs['final'] : 0 o algo parecido
print("Ejemplo de funcion con operador ternario")
def sumador(**kwargs):
    inicial = kwargs['inicial'] if 'inicial' in kwargs else 0
    final = kwargs['final'] if 'final' in kwargs else inicial
    resultado = 0
    for x in range(inicial, final + 1):
        resultado += x

    return resultado

print(sumador(inicial=15))
print(sumador(final=15))
print(sumador(inicial=8, final=15))


# funciones anónimas(lambda)
print("\n****************Funciones anónimas (Lambdas) ********************")
print("\n-Sin parámetros:")
print("anonima = lambda: print ('hola')")
print("anonima()")
print("*Resultado de esa función:")
anonima = lambda: print("hola")
anonima()

print("\n-Con parámetros:")
print("anonima = lambda nombre, hora: print ('Hola', nombre, hora)")
print("anonima('Pepe', '18:26')")
anonima = lambda nombre, hora: print("Hola", nombre, hora)
print("*Resultado de esa función:")
anonima("Pepe", "18:26")

print("\n-Con devolucion de parámetros:")
print("sumatoria = lambda x: x+x")  # Va a devolver el resultado de x+x
sumatoria = lambda x: x+x
print("print(sumatoria(5))")
print("*Resultado de esa función:")
print(sumatoria(5))

print("\n-Con devolucion de varios parámetros:")
print("sumatoria = lambda x: [x+x, x+y] ")  # Va a devolver el resultado de x+x
sumatoria = lambda x, y: [x+x, x+y]
print("print(sumatoria(5, 2))")
print("*Resultado de esa función:")
print(sumatoria(5, 2))
