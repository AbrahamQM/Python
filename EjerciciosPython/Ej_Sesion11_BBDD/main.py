# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas:
# la columna id de tipo entero,
# la columna nombre que será de tipo texto
# la columna apellido que también será de tipo texto.
#
# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 5 alumnos a la tabla.
#
# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
import sqlite3


def registros():
    conn = sqlite3.connect('alumnos.db', isolation_level=None)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    global identificador
    identificador = len(cursor.fetchall())

    cursor.close()
    conn.close()


def insertar():
    conn = sqlite3.connect('alumnos.db', isolation_level=None)
    cursor = conn.cursor()

    global identificador
    identificador += 1
    print("\n*** Agregar alumno a la base de datos ***\n")
    nombre = input("*Introduzca nombre del alumno:\n")
    apellidos = input("*Introduzca apellidos del alumno:\n")
    query = '''INSERT INTO users(id, 'nombre', 'apellidos') VALUES(?, ?, ?)'''
    rows = cursor.execute(query, (identificador, nombre.capitalize(), apellidos.capitalize()))

    cursor.close()
    conn.close()


def buscar():
    name = input("Introduzca nombre del alumno a buscar:\n")
    conn = sqlite3.connect('alumnos.db', isolation_level=None)
    cursor = conn.cursor()

    rows = cursor.execute(f'SELECT * FROM users WHERE nombre="{name.capitalize()}"')
    for row in rows:
        print(row)

    cursor.close()
    conn.close()


def main():
    mas = True
    global identificador
    print("****-- Bienvenido al programa base de datos de alumnos. --****")
    registros()
    while identificador < 5 or mas:
        print(f'-Actualmente hay {identificador} registros en la base de datos')
        if identificador >= 5:
            print("\n*¿Desea añadir otro alumno? S/N")
            otro = input()
            if otro.lower() != 's':
                mas = False
            else:
                insertar()
        else:
            insertar()

    print("\n*¿Desea buscar alumno? S/N")
    otro = input()
    if otro.lower() != 's':
        buscaAlumno = False
    else:
        buscaAlumno = True
    while buscaAlumno:
        buscar()
        print("\n*¿Desea buscar otro alumno? S/N")
        otro = input()
        if otro.lower() != 's':
            buscaAlumno = False
        else:
            buscaAlumno = True



if __name__ == '__main__':
    main()
