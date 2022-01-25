####### Sesion 4 CONTROL DE FLUJO  ################
# Test de veracidad
# if condicion:
#    acciones


# Operadores relacionales:
# > mayor que
# > menor que
# >= Mayor o igual
# <= Menor o igual
# == Exactamente igual
# != Distinto

a = 5
b = 6
c = 7

print("a: ", a)
print("b: ", b)
print("c: ", c)
# Uso:
print("\n--Uso de condicionales:")

resultado = a < b
print("a < b: ", resultado)

resultado = a > b
print("a > b: ", resultado)

resultado = a >= b
print("a >= b: ", resultado)

resultado = (a == b)  # no es necesario porner el paréntesis, es solo para que quede mas claro
print("a == b: ", resultado)

print("a != b: ", a != b)  # También se puede imprimir sin guardarlo en ninguna variable

print("\n-Condicionales anidados")
# Resultado = a > 5 and c < 7 El proceso interno de la comprobación sería:
# 1º: resultado = (False and c < 7)
# 2º: resultado = (False and False)
# 3º: resultado = False

print("a > 5 and c < 7: ", a > 5 and c < 7)  # se puede usar and o &
print("a >= 5 & c <= 7: ", a >= 5 & c <= 7)

print("a == 5 and c == 7: ", a == 5 and c == 7)  # ATENCIÓN si uso & da false, (&) no es idéntico a usar (and)

print("\n-3 condiciones:")
resultado = ((a >= 5 or c > 7) and (b == 5))
print("((a >=5 or c > 7) and (b==5)): ", resultado)
# resultado = ((a >= 5 or c > 7) and (b == 5))
# 1º: resultado = (True or False) and (False)
# 2º: resultado = (True and False)
# 3º: resultado = False

print("\n--Tablas de la verdad:")
print("-Tabla de la verdad de AND o (&):")
print("T y T", True and True)
print("T y F", True and False)
print("F y F", False and False)
print("F y T", False & True)

print("-Tabla de la verdad de or:")
print("T or T", True or True)
print("T or F", True or False)
print("F or F", False or False)
print("F or T", False or True)

print("-Tabla de la verdad de XOR(^):")
print("T xor T", True ^ True)
print("T xor F", True ^ False)
print("F xor F", False ^ False)
print("F xor T", False ^ True)

# Uso del IF:
# if condicion:
#     acciones en if 1
#     acciones en if 2
#     acciones en if 3
# acciones fuera del if
# Se termina con ':' y todas las acciones irán tabuladas o con espacios dentro de ese if. (no hay llaves)
# Ojo, no mezclar tabulador y espacios, todas las acciones deben estar "tabuladas" de la misma forma!!
print("\n--Uso de if:")
print("(OJO) a =", a)
print("\n-Ejemplo 1 if a == 4:")
if a == 4:
    print("Estoy en el if")
    print("segunda línea dentro el if")
print("Estoy fuera del if (sin tabular)")

print("\n-Ejemplo 2 if a == 5:")
if a == 5:
    print("Estoy en el if")
    print("segunda línea dentro el if")
print("Estoy fuera del if (sin tabular)")

print("\n--Múltiples comparaciones: if a == 5 and b <= 6:")
if a == 5 and b <= 6:
    print("a es igual a 5 y b <= 6")
    print("segunda línea dentro el if")
print("Estoy fuera del if (sin tabular)")

print("\n-Uso de (elif): sólo si no se cumple el if, comprueba el elif") # Podemos tener tantos elif cono queramos
# Si se cumple el if, no ejecuta el elif!!!!
print("\n-Ej1: if a == 5 and b >= 7(FALSE)\nelif c == 7(TRUE)\nResultado:")
if a == 5 and b >= 7:
    print("Estoy dentro del if")
    print("segunda línea dentro el if")
elif c == 7:
    print("Estoy en el (elif)")
print("Estoy fuera del (if) y el (elif)")

print("\n-Ej2: if a == 5 and b >= 6(TRUE)\nelif c == 7(TRUE)\nResultado:")
if a == 5 and b >= 6:
    print("Estoy dentro del if")
    print("segunda línea dentro el if")
elif c == 7:
    print("Estoy en el (elif)")
print("Estoy fuera del (if) y el (elif)")

print("\n-Ej3: if a == 5 and b >= 7(FALSE)\nelif c == 8(FALSE)\nResultado:")
if a == 5 and b >= 7:
    print("Estoy dentro del if")
    print("segunda línea dentro el if")
elif c == 8:
    print("Estoy en el (elif)")
print("Estoy fuera del (if) y el (elif)")

print(
    "\n-Uso de (else): sólo se ejecutara si ninguna de las condiciones if o elif se cumple")# Sólo podemos tener un else
print("\n-Ej1: if a == 5 and b >= 7(FALSE)\nelif c == 7(TRUE)\nelse:\nResultado:")
if a == 5 and b >= 7:
    print("Estoy dentro del if")
    print("segunda línea dentro el if")
elif c == 7:
    print("Estoy en el (elif)")
else:
    print("Estoy en el (else)")
print("Estoy fuera del (if), el (elif) y el (else)")

print("\n-Ej2: if a == 5 and b >= 7(FALSE)\nelif c == 8(FALSE)\nelse:\nResultado:")
if a == 5 and b >= 7:
    print("Estoy dentro del if")
    print("segunda línea dentro el if")
elif c == 8:
    print("Estoy en el (elif)")
else:
    print("Estoy en el (else)")
print("Estoy fuera del (if), el (elif) y el (else)")
