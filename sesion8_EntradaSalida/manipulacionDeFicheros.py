#  Vamos a leer un fichero
# Modos de apertura de ficheros:

# r: lectura (sólo permite leer del fichero)
# a: append(adjuntar, añadir al final)
# w: escritura(sólo lee, pero no escribe)
# x: create

# t: texto
# b: binary

# +: 'w+' es igual a 'rw'
#    'wb+' es lectura y escritura binaria
#  VER DOCUMENTACIÓN PARA MAS OPCIONES Y DATOS
# ********************************************************************

# f = open('pruebas', 'x') Una vez creado, da error si lo volvemos a intentar
f = open('pruebas', 'r')
print("print(f.read()):", f.read())
print("-----Las buenas prácticas dicen que abramos, guardemos el contenido en una variable y cerremos Ej:")
print("f = open('pruebas', 'r')\ndatos = f.read()\nf.close()")
datos = f.read()
f.close()

print("**Podemos poner el número de bytes que queremos que lea así f.read(18), para que solo lea los primeros x bytes")
print("-cada caracter ocupa un byte")

print("\n-Para leer línea a línea usar: f.readline()")
print("f = open('pruebas', 'r')\ndatos = f.readline()\ndatos += f.readline()\nf.close()\nprint(datos):")
f = open('pruebas', 'r')
datos = f.readline()
datos += f.readline()
f.close()
print(datos)

print("\n-Lo haremos con un 'while'")
print("*while datos != '':\n  datos = f.readline()\n  print(datos)")
datos = None
f = open('pruebas', 'r')
while datos != "":
    datos = f.readline()
    print(datos)
f.close()

print("*while len(datos) > 0:\n  datos = f.readline()\n  print(datos)")
datos = "." # Le pongo '.' por que si es None da error y si es '' len(datos) es 0 y no hace nada
f = open('pruebas', 'r')
while len(datos) > 0:
    datos = f.readline()
    print(datos)
f.close()


print("**********Leer todo el fichero guardándola en una lista con f.readlines() EN PLURAL***************")
print("datos = f.readlines()\nprint(datos):")
f = open('pruebas', 'r')
datos = f.readlines()
f.close()
print(datos)


print("\n\n------------------ Escribir en ficheros ---------------------")
print("--Crear y escribir fichero:\nf = open('miFichero.txt', 'w')\nf.write('datos')\nf.write('datos2')")
f = open('miFichero.txt', 'w')
f.write("datos\n")
f.write("datos2")
f.close()

print("--Añadir al fichero miFichero2.txt igual pero con 'a' en lugar de 'w'")
f = open('miFichero2.txt', 'a')
f.write("mas datos\n")
f.write("mas datos2\n")
f.close()


print("\n--Añadir una lista al fichero por líneas con writelines() [OJO, no añade \\n]")
print("-1º vacío miFichero2 con:\nf = open('miFichero2.txt', 'w')\nf.close()")
f = open('miFichero2.txt', 'w')
f.close()

lista = ['1 linea\n', '2 linea\n', '3 linea\n']
print('-2º Creo la lista:', lista)
print("-3º Escribo la lista en la línea con: \nf.writelines(lista)")
f = open('miFichero2.txt', 'a')
f.writelines(lista)
f.close()





