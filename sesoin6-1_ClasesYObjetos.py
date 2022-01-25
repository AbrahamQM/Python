
print("******************** Sesión 6 Clases y objetos *****************************")
print("\n******OJO IMPORTANTE, por convención si un atributo o método de la clase comienzan por '_',"
      " no deberíamos modificarlos")

print("----------------CLASES DINÁMICAS (cada objeto instanciado tiene sus métodos y atributos individuales "
      "---------------------\n")


class Dino:  # Declaración de la clase
    _encendido = False

    def enciende(self):  # Método dentro de la clase Dino
        self._encendido = True  # Ponemos 'self.' para que cambie el valor de la variable, en lugar
        # de crear una nueva variable local al método

    def apaga(self):
        self._encendido = False

    def isEncendido(self):
        return self._encendido


print("Creamos una instancia de Dino así: d = Dino()")
d = Dino()  # Instanciación de la el objeto de tipo Dino

d.enciende()
print("\nd.enciende()\nDino esta encendido: print(d._encendido)\n", d._encendido)

d.apaga()
print("\nd.apaga()\nDino esta encendido: print(d._encendido)\n", d._encendido)

# ************Después de crear el método isEncendido************
print("\n-Hemos creado el método isEncendido.\nDino esta encendido: print(d.isEncendido())\n", d.isEncendido())

print("\n-Creamos otra instancia de Dino así: 'd1 = Dino()' y lo encendemos")
d1 = Dino()
d1.enciende()
print("+Para comprobar que son dos objetos diferentes")
print("Vemos el estado de d encendido:", d.isEncendido())  # para comprobar que son dos objetos diferentes
print("Vemos el estado de d1 encendido:", d1.isEncendido())

print("\n-----------CLASES ESTÁTICAS (cada objeto instanciado comparte sus métodos y atributos con los demás "
      "objetos de esa clase ------------\n")

print("A diferencia de las clases dinámicas, las estáticas no se instancian,"
      ", comparten el espacio de memoria y se usan directamente")


class Estatica:
    numero = 1

    def incrementa():
        Estatica.numero += 1


print(Estatica.numero)
Estatica.incrementa()
print(Estatica.numero)

Estatica.incrementa()
print(Estatica.numero)

Estatica.incrementa()
print(Estatica.numero)

# ************* HERENCIAS entre clases (is a)***********************
print("\n****************** Herencias entre clases (is a)*************************")
print("Se declaran poniedo entre () el nombre de la clase de la que hereda.\n")


class Juguete:
    encendido = False

    def enciende(self):  # Método dentro de la clase Dino
        self.encendido = True  # Ponemos 'self.' para que cambie el valor de la variable, en lugar
        # de crear una nueva variable local al método
        print("..Encendiendo el Juguete")

    def apaga(self):
        self.encendido = False
        print("..Apagando el Juguete")

    def isEncendido(self):
        return self.encendido


class Potato(Juguete):
    orejas = 0

    def quitarOreja(self):
        self.orejas -= 1

    def ponerOreja(self):
        self.orejas += 1


p = Potato()
p.ponerOreja()
p.ponerOreja()
p.quitarOreja()
print("Orejas en Potato 'p': ", p.orejas)
print("-Endendemos 'p' para comprobar que podemos acceder a los métodos de la clase padre 'p.enciende()'")
p.enciende()
print("Apagamos 'p'")
p.apaga()
print("¿'p' esta encendido? (Accedemos a un atributo de la clase padre):", p.isEncendido())

print("\n\n************* Herencia múltiple **************")
print("-Creamos un objeto que hereda de Potato y de Puzzle a la vez")


class Puzzle:
    piezas = 0

    def definirPiezas(self, numero):
        self.piezas = numero
        print("+Ahora este objeto Puzzle tiene", self.piezas, "piezas.")


class MissPotato(Puzzle, Potato):
    lazo = False

    def ponerLazo(self):
        self.lazo = True


mP = MissPotato()
print("\n-Ahora 'mP' tiene", mP.orejas, "orejas. Añadimos una oreja con 'mP.ponerOreja'")
mP.ponerOreja()
print("\n-Accedemos a un atributo de Potato 'orejas', Tiene orejas:", mP.orejas)

print("\n-Ahora accedemos a un método de la clase Puzzle 'mp.definirPiezas(50)'")
mP.definirPiezas(50)
print("\n-Imprimimos el nº de piezas de 'mP':", mP.piezas)
print("\n--Ahora accedemos a atributos y métodos de la clase Juguete ")
print("-Esta encendido mP?:", mP.isEncendido())
print("-Encendemos 'mP'")
mP.enciende()
print("-Esta encendido mP?:", mP.isEncendido())

print("Para Acceder a los métodos y atributos de una clase y objeto poner dir(clase u objeto):")
print("Hacemos print(dir(mP)):\n", dir(mP))
print("Hacemos dir(Juguete):\n", dir(Juguete))

