##SESION 3
#variables mutables o inmutables
print("\n\n------Sesion 6 tipos mutables e inmutables--------")
print("\n---Tipos de datos inmutables")
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
print("Al volver a poner el valor anterior, python vuelve a apuntar a la dirección de la primera inicialización de la variable\n\n") 

print("---Tipos de datos mutables")
            #####DATOS MUTABLES#####
#Las listas son un tipo de dato mutable, a diferencia de las tuplas.
#pueden tener valores duplicados
print ("\n\n-Listas:")
print("Creamos una lista, a diferencia de las Tuplas, las listas se declaran con [ ] en lugar de ( )")
print ("Declaramos la lista así: miLista = [valor1, valor 2, valor 3 ]   \nLos valores pueden ser tambien el contenido de una variable anterior")
miLista=[ 5, 'O', 'A', a, 'l' ]
print (miLista)

print("\n-Para acceder al nº de elementos usar:\nlen(miLista):", len(miLista))
print("\n-Para acceder al tipo de dato que es miLista usar:\ntype(miLista):", type(miLista))

print("\n-Ahora voy a modificar el valor de la posición o ->'z' asi: miLista[0] = 'z'")
miLista[0] = 'z'
print (miLista)
print("Como podemos comprobar, las listas si son mutables\n")

print("-Para añadir elementos a la lista, se hace así: miLista.append('a')")
miLista.append('a')
print(miLista)
miLista.append('cadena de caracteres')
print(miLista)


print("\n-Para eliminar elementos a la lista, se hace así: miLista.remove('a')")
miLista.remove('a')
print(miLista)

print("Agregar(concatenar) una lista a otra se hace así: miLista.append(otraLista)")
print("otraLista = ['a', 18, 'g']")
otraLista = ['a', 18, 'g']
print(otraLista)
print("miLista.append(otraLista)  OJO, tomara otraLista como si fuera un solo valor SON LISTAS ANIDADAS")
miLista.append(otraLista)
print(miLista)

#DICCIONARIOS son idénticos a json, de hecho son intercambiables
#se declaran usando { }
print ("\n\n-Diccionarios:")
diccionario = { "Clave1": "valor1", "Clave 2": "valor2",  "Clave3": "valor3",  "Clave4": "valor4"}
print (diccionario)
print("Para imprimir un elemento concreto, lo hacemos a través de la clave asi:")
print("print(diccionario['Clave 2'])")
print(diccionario['Clave 2'])
print("Cambiamos un valor asi: diccionario['Clave 2'] = 99")
diccionario['Clave 2'] = 99
print(diccionario)

print("--Podemos eliminar claves de un diccionario de 2 formas:")
print("-POP: diccionario.pop('Clave 1')     *****  NOS DEVUELVE  EL VALOR ASOCIADO")
elementoViejo = diccionario.pop('Clave1')
print (diccionario)
print("Ha devuelto:")
print(elementoViejo)
print("-DEL: del diccionario['Clave 2']       *****NO NOS DEVUELVE NADA")
del diccionario['Clave 2']
print (diccionario)

##CONJUNTOS o SETS es una lista pero no pueden tener valores duplicados
#se declaran usando { }
print("\n\n-Conjuntos o sets:")
print("Creamos un conjunto así conjunto = { 1, 2, 3, 1 ,2 , 5} sólo se van a añadir los valores que no existieran anteriormente")
conjunto = { 1, 2, 3, 1 ,2 , 5}
print (conjunto)

print("\n-Operaciones matemáticas de conjuntos:")
print("-Union: une ambos sets obviando los valores repetidos")
print("Creamos un conjunto de num pares y otro de num coorelativos, luego los unimos asi: pares | coorelativos")
pares = {0, 2, 4, 6, 8}
coorelativos = {1, 2, 3, 4, 5}
print(pares)
print(coorelativos)

print("Ahora implimimos la union de pares y coorelativos:")
total = pares | coorelativos
print(total)
print("nos ha mostrado todos los elementos No repetidos, resultado de unir ambos sets con '|'")

print("\n-Intersección: nos muestra que valores hay en ambos sets simultaneamente")
print("una intersección se obtiene con & así: inter = pares & coorelativos")
inter = pares & coorelativos
print(inter)

print("\n-Diferencia, nos devuelve los números que están en el primer set, pero no en el segundo")
print("una diferencia se obtiene con - así: dif = pares - coorelativos")
dif = pares - coorelativos
print(dif)
print("Compara los el primer set con los valores del segundo")

print("\n-Diferencia simétrica: devuelve los valores que solo están en uno de los sets")
print("unadiferencia simetrica se hace con el caracter ^ así: dSim = pares ^ coorelativos")
dSim = pares ^ coorelativos
print(dSim)

###############RESUMEN DE TIPOS DE DATOS###################
                ####Tipos de datos que usamos en python####
print("\n\n---Resumen de tipos de datos. Ver en el archivo")
numeros = 5 #números
cadenas = 'hola' #Cadenas de caracteres
booleano = True #boolean
flotante = 5.3 #Flotantes
lista = ['a', 5, 'T'] #Listas
tupla = ('a', 'b', 8) #Tuplas
diccionario = { 'clave': 1, 'clave2': 'valor2'} #Diccionarios
conjunto = {1, 2, 3, 4, 1, 2, 3, 4, 'loco'} #Sets

####################Metodos de los tipos String############
print("\n\n---Metodos de los tipos String, \ncreo mitexto ='hola, esto es un textO'")
mitexto= "hola, esto es un textO" #hemos puesto la O en mayusculas adrede para hacer pruebas
print(mitexto)

print("\n-Capitalizamos todo el texto asi: mitexto.capitalize()")
print(mitexto.capitalize())
print("OJO no modifica el valor, solo nos devuelve el valor capitalizado mitexto es:")
print(mitexto)

print("\n-Capitalizamos la primera letra de cada palabra así: mitexto.title()")
print(mitexto.title())

print("\n-Todo en minúscula asi: mitexto.lower()")
print(mitexto.lower())

print("\n-Todo en mayúscula asi: mitexto.upper()")
print(mitexto.upper())

print("\n-Reemplazar una letra por otra así: mitexto.replace( 'a' , 'o')")
print(mitexto.replace( 'a' , 'o'))
print("o simplemente rrellenar los espacios asi: print(mitexto.replace( ' ' , '*')")
print(mitexto.replace( ' ' , '*'))

print("\n-Buscar una letra o texto así: mitexto.find('esto')")
print(mitexto.find("esto"))
print("nos devuelve en que posición de la cadena aparece o comienza esa palabra por primera vez: mitexto.find('u')")
print(mitexto.find("u"))

print("\n-Convertimos mitexto en una lista así: mitexto.split()")
print(mitexto.split())
print("O, determinando el caracter que lo separa así: mitexto.split('o')")
print(mitexto.split('o'))

print("\n-Convertir una lista en texto asi: ' '.join(listaTexto)     primero convertimos mitexto a lista (listaTexto)")
listaTexto = mitexto.split()
print("listaTexto es:")
print(listaTexto)
print("haciendo  ' '.join(listaTexto) :")
print( ' '.join(listaTexto))
print("Ahora en vez de ' ' vamos a poner '$' o lo que queramos")
print( '$'.join(listaTexto))

print("\nPara ver todas las opciones de los string ponemos help(str)--lo comento para evitar que cargue toda la ayuda")
# help(str)


print("\n-Combinamos métodos así: mitexto.replace(',', ' ').lower().split()  Conseguimos una lista en minúsculas sin ','")
print(mitexto.replace(',', ' ').lower().split())


###Introduccion a los operadores
print("\n\n-----Introduccion a los operadores")
#--Asignación variable = 5
print("-Asignación variable = 5")
a=6
b=4
print("a=" , a, "b=",  b)
print ("modificadores +=, -=, *=, /= 'modifican' el valor de a es similar a : a= a +5")
print("a += 5: ")
a +=5
print("a= ", a)
print("a -= 5: ")
a -=5
print("a= ",a)
print("a **= b: ")
a **= b
print("a=", a)



#--Aritméticos:
a=6
b=4
print("-Aritméticos +, -, *, /, %, **, //")
print("a=" , a, "b=",  b)
#suma 1 + 4
print("suma a + b: print(a+b)")
print(a+b)
#resta 5 - 3
print("resta a - b: print(a-b)")
print(a-b)
#multiplicación  5 * 6
print("multiplicación  a * b: print(a*b)")
print(a*b)
#division 10 / 5       y    división sin decimales 5//2
print("division a / b: 1-print(a/b) ->Muestra resultado real Ó 2-print(a//b) Muestra solo la parte entera")
print("1-", a/b)
print("2-", a//b)
#Resto de la operacion
print("Resto de la operacion: print(a%b)")
print(a%b)

#Potenciacion a ** b es sinónimo de elevar un número al otro
print("Potenciación a**b es elevar A a B : 3**3 = 27")
print("a = 6, b=4,        a**b = ", a**b) 
