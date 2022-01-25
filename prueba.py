print("------Ejemplos básicos--------")
print ("hola")
print("adios")

x="5"
print("x vale " + x)
################     cLASE#######################
#Ejemplo de clase
print("------Ejemplo de clase--------")
class miclase:
    def suma(self, a, b):
        return a + b
    
datos = miclase()
print(datos.suma(2,2))
########               TIPADO               ################
#tipado dinámico, "el interprete de phyton determina que tipo de datos es
print("------Ejemplo de tipado--------")
a = 5 #es de tipo int
b = "hola" #es de tipo string
c = 2.2 # es de tipo float

print (a)
print(type(a))
print(b)
print(type(b))
print (c)
print(type(c))

a=a+1
print(a)
######################    CONVERSION DE TIPOS ##################
print("------Ejemplo de conversión de tipos--------")
d=str(a) + b
print(d)

### VER LAS LIBRERIAS INSTALADAS CON "pip"########
# pip list
# pip show nombreDelPaquete  muestra los datos relevantes a el paquete

### PARA CREAR DISTINTOS ENTORNOS VIRTUALES###########
#USAR LA FUNCION pipenv shell ESTANDO  DENTRO DE  LA CARPETA DEL PROYECTO

###INSTALAR Y DESINSTALAR PAQUETES EN EL ENTORNO VIRTUAL####
#pipenv install nombreDelPaquete
#pipenv unisnstall nombreDelPaquete

###SALIR DEL ENTORNO VIRTUAL##
#exit

###CREAR ARCHIVO CON TODAS LAS DEPENDENCIAS  NECESARIAS PARA NUESTRO PROYECTO
#pipenv lock

##SESION 3
#variables mutables o inmutables
print("\n\n------tipos mutables e inmutables--------")
a=5
print ("\ntipo de variable a:" )
print (type(a))
print ("puntero a memoria de a es:" )
print(id(a))
print ("-Asignamos otro valor a la variable a")
a=6
print ("--Python asigna un nuevo espacio de memoria automáticamente, Ahora el  puntero a memoria de a es:" )
print(id(a))

print ("--Ahora a le asignamos el mismo valor del principo, python recupera el espacio de memoria anterior")
a=5
print(id(a))

print ("\nEso quiere decir que los valores numéricos son inmutables")
print ("\n--Los valores de tipo Texto y Tuplas, tambien son inmutablesson inmutables")
print("\n--Ej con cadenas string:")
texto = "Hola"
print(texto)
print ("Intentanmos cambiar el contenido de texto (hola) a (Gola) usando texto[0] igual que en un array")
print("texto[0] =  'G'")
print(" Muestra el error: TypeError: 'str' object does not support item assignment")
print("--Lo que significa que las cadenas de texto son inmutables")
print( "\n Las tuplas son listas que se declaran así: tupla = (valor1, valor2, valor3, ...)")
print ("-Ahora vamos a declarar una tupla así:  miVariable = ('a', 2, 'b')")
miVariable = ('a', 2, 'b')
print(miVariable)
print ("ID:")
print(id(miVariable))
print("Tipo:")
print (type(miVariable))
print("-Añadimos un valor a nuestra tupla asi: miVariable = ('a', 2, 'b', 'c')")
print ("Ahora python guarda esa tupla en otro espacio de almacenamiento:")
miVariable = ('a',  2,  'b',  'c')
print(miVariable)
print ("ID:")
print(id(miVariable))
print("Pasamos a los valores niniciales miVariable = ('a', 2, 'b')")
miVariable = ('a', 2, 'b')
print(miVariable)
print ("ID:")
print(id(miVariable))
print("Al volver a poner el valor anterior, python vuelve a apuntar a la dirección de la primera inicialización de la variable") 

