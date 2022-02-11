import sqlite3

# Abrir bbdd con la función nombreDeInstanciaConección = sqlite3.connect('nombre de la bbdd')

conn = sqlite3.connect('miaplicacion.db')

# Generar un cursor
cursor = conn.cursor()

# Ejecutar un comando de sql y asignarlos a una variable llamada por convención row o rows
rows = cursor.execute('SELECT * FROM users')

print('rows es del tipo:', type(rows))

# Ver los datos que ha obtenido:
print("\n--Ver los datos que ha obtenido:\nfor row in rows:\n   print(row):\n")
for row in rows:
    print(row)


# Filtrar uno de los datos y guardarlo en el cursor
print("\n--Filtrar uno de los datos y guardarlo en el cursor con:\nrows = cursor.execute('SELECT * FROM users"
      " WHERE username='Abraham'')\n")
rows = cursor.execute('SELECT * FROM users WHERE username="Abraham"')

for row in rows:
    print(row)



# Cierre del cursor
cursor.close()

# Para cerrar la conección con bbdd:
conn.close()
