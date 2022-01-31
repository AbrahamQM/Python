import pickle
# ***   Serializar consiste en convertir una representación de un programa
# a una secuencia de datos que podamos guardar en un fichero

# ***   Deserializar es justo lo contrario


# Declaramos una clase con algún método

class Juguete:
    nombre = ''
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def getNombre(self):
        return self.nombre

j1 = Juguete('potato', 10.5)

print("**Para guardar los datos de forma serializada debemos abrirlos usando f = open('datos.bin', 'wb'), "
      "\n-'wb' porque es en modo escritura binaria")
f = open('datos.bin', 'wb')
print("**Invocamos a pickle el método dump('datosAGuardar', 'FicheroAbierto con 'wb') para que descargue así:"
      "\npickle.dump(j1, f)")
pickle.dump(j1, f)
f.close()

print("\n-----Ahora obtenemos los datos serializados")
print("**Para obtener los datos de forma serializada debemos abrirlos usando f = open('datos.bin', 'rb'),"
      "\n-'rb' porque es en modo lectura binaria")
f = open('datos.bin', 'rb')
print("\n**Invocamos el método load(ficheroAbiertocon'rb') de pickle:\njuguete1 = pickle.load(f)")
juguete1 = pickle.load(f)
print("-type(juguete1):\n", type(juguete1),
      "\n-juguete1.getNombre():\n", juguete1.getNombre(),
      "\n-juguete1.precio:\n",  juguete1.precio)


