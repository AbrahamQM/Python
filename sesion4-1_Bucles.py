##Bucles condicionales

# while
# while mientras la condicion sea true:
#   acciones1
#   acciones2

contador = 1
print("-Ejemplo básico de while:")
while contador <= 5:
    print("contador vale", contador)
    contador += 1
print("Fuera del while")

# Romper el bucle con break y continue
contador2 = 1
print("\n-Ejemplo de BREAK, mostrar números del 1 al 10 y, romper el bucle en el 4")
while contador2 <= 10:
    print("Contador vale", contador2)
    if contador2 == 4:
        print("if contador == 4: Rompo el bucle con break")
        break

    contador2 += 1

print("Fuera del while")

contador3 = 0
print("\n-Ejemplo de CONTINUE, mostrar números pares del 1 al 10")
while contador3 <= 10:
    contador3 += 1
    if contador3 % 2 == 0:
        print(contador3, "es par-------------------")
        continue
    print("Contador vale", contador3, "es impar")
print("Fuera del while")

##Uso del for
# for valor in cosa:

print("\n--Ejemplo básico de for con lista: \nfor valorActuel in lista:\n    print(valorActual)")
lista = [1, 2, 3, 'a', 5]
for valorActual in lista:
    print(valorActual)
print("-También se puede hacer con tuplas:\nfor valorActual in tupla:\n print(valorActual)")
tupla = (1, 2, 3, 'c', 'd')
for valorActual in tupla:
    print(valorActual)

print("\n-Ejemplo con rango (range(a,b)):\nfor numero in range(5, 10)\n    print(numero) ")
for numero in range(5, 10):
    print(numero)
print("Si ponemos un rango, este:\n-Incluye el nº inicial\n-Excluye el nº final")

print("\n-Ejemplo con rango (range(a)):\nfor numero in range(5)\n    print(numero) ")
for numero in range(5):
    print(numero)

print("\n-Ejemplo con nº elementos de lista len(lista):\nfor numero in range(len(lista)):\n    print(lista[numero])")
print("len(lista) es:", len(lista))
for numero in range(len(lista)):
    print(lista[numero])

lista = ["hola", "mensaje", "adiós"]
print("\n-Ejemplo con el código:\nfor palabra in lista:\n   if palabra == 'mensaje':"
      "\n       print('He encontrado la palabra mensaje en la lista:')"
      "\n       break"
      "\n*La lista es:", lista)
print("*Resultado del código:")
for palabra in lista:
    if palabra == "mensaje":
        print("He encontrado la palabra mensaje en la lista")
        break

# Ojo ese último código se podría sustituir por:
print("\n**Ojo ese último código se podría sustituir por:"
      "\nif 'mensaje' in lista:"
      "\n   print('He encontrado la palabra mensaje')\n*Resultado del código:")
if "mensaje" in lista:
    print("He encontrado la palabra mensaje")

print("\n**Tambien se puede usar la negación así:"
      "\nif 'cosa' not in lista:"
      "\n   print('Lista no contiene la palabra cosa')\n*Resultado del código:")
if "cosa" not in lista:
    print("Lista no contiene la palabra cosa")

# Ordenar listas con sorted()
print("\n**Ordenamos las listas")
print("\n-Ordenamos la lista alfabéticamente asi print(sorted(lista)), da como resultado:", sorted(lista))
print("\n-Igual pero en sentido contrario print(sorted(lista, reverse)):",
     sorted(lista, reverse=True))

lista = [3, 4, 1, 2, 5]
print("\n-Ahora vamos a ordenar esta lista de números sin ordenar:", lista)
print("Lista ordenada:", sorted(lista))
print("Lista ordenada a la inversa con print sorted(lista, reverse=True))", sorted(lista, reverse=True))

# Equivalencia al switch
print("\n***Sentencia que equivale(python 3.10->) a switch es:\nmatch cosa:\n case 1:\n   contenido\n case 2:\n       ...")
print("\n-Ejemplo:")
valor = 3
match valor:
    case 1:
        print("Valor es 1")
    case 2:
        print("Valor es 2")
    case 3:
        print("Valor es 3")
    case 4:
        print("Valor es 4")
    case 5:
        print("Valor es 5")

# Palabra reservada pass es sinonimo de ignorar, se usa para los momentos en los que estamos obligados
# A implementar un código pero todaía no sabemos o queremos hacerlo. Evita que el programa falle
print("\n**VER CÓDIGO, Palabra reservada pass:\n El código: (for palabra in lista:) si no ponemos las acciones da este error:"
      "\nIndentationError: expected an indented block after 'for' statement")
for palabra in lista:
    pass
print("\nEn cambio si ponemos ignorar con la palabra pass así:")
print("for palabra in lista:\n  pass\nYA NO MUESTRA EL ERROR")