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
print("------Ejemplo de clonversión de tipos--------")
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

