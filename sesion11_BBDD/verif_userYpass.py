# Ej Un sistema de verificación de usuario y contraseña
# Agregar registro
# listar registro
# borrar registro
# LAS FUNCIONES Agregar registro, listar registro, borrar registro Y EL MENÚ HAN SIDO IMPLEMENTADAS POR MÍ
# (no aparecen en el video de la sesión).

import getpass
import sqlite3

print("\n******* Ej: Un sistema de verificación de usuario y contraseña *******\n")


def main():
    mas = True
    while mas:
        print("\n\n**** MENU ****")
        opcion = input("**1.-Agregar usuario\n**2.-Hacer login\n**3.-Listar todos\n**4.-Borrar por id\n**5.-salir):\n")
        if opcion == '1':
            insert()
        elif opcion == '2':
            login()
        elif opcion == '3':
            listar()
        elif opcion == '4':
            borrar()
        elif opcion == '5':
            mas = False
        else:
            print("-----Opción Errónea-----")


def borrar():
    identificador = input("-Id a borrar: ")
    conn = sqlite3.connect("miaplicacion.db", isolation_level=None)
    cursor = conn.cursor()

    query = f'DELETE FROM users WHERE id="{identificador}"'
    print("query a ejecutar:", query)

    cursor.execute(query)
    # conn.commit()  # Para enviar los cambios a la base de datos SIEMPRE QUE CAMBIEMOS COSAS si no ponemos:
    # isolation_level=None al realizar la conexión
    cursor.close()
    conn.close()


def listar():
    conn = sqlite3.connect("miaplicacion.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users"
    print("\n-Query a ejecutar:", query)

    rows = cursor.execute(query)

    for row in rows:
        print(row)

    cursor.close()
    conn.close()


def login():
    username = input("\nNombre de usuario: ")
    password = getpass.getpass()

    if verifica_credenciales(username, password):
        print("\nLogin correcto!!")
    else:
        print("\nError en login. :(")


def insert():
    nombre = input("\n-Nombre: ")
    identificador = input("-Id: ")
    password = getpass.getpass("-Contraseña: ")
    insertar_usuario(identificador, nombre, password)


def verifica_credenciales(username, password):
    conn = sqlite3.connect("miaplicacion.db")
    cursor = conn.cursor()

    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
    print("\n-Query a ejecutar:", query)

    rows = cursor.execute(query)
    data = rows.fetchone()  # El método fetchone(), va a devolver sólo un elemento que coincida

    cursor.close()
    conn.close()
    if data is None:
        return False
    else:
        return True


def insertar_usuario(identificador, usuario, clave):
    conn = sqlite3.connect("miaplicacion.db", isolation_level=None)
    cursor = conn.cursor()

    query = '''INSERT INTO users(id, username, password) VALUES(?, ?, ?)'''
    print("query a ejecutar:", query)

    rows = cursor.execute(query, (identificador, usuario, clave))
    print(type(rows))
    # conn.commit()  # Para enviar los cambios a la base de datos SIEMPRE QUE CAMBIEMOS COSAS si no ponemos:
    # isolation_level=None al realizar la conexión
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
