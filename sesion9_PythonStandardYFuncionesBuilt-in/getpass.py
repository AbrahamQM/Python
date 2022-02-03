from getpass4 import getpass


print("Para ocultar la contraseña al escribirla usar getpass getpass solo funciona al ejecutarlo"
      " desde fuera de intellij")

user = input("¿username?: ")
passwd = getpass("Password: ")

print("Para ocultar la contraseña al escribirla usar getpass getpass solo funciona al ejecutarlo"
      " desde fuera de intellij")


print(f'User: {user}, Password:{passwd}')
input()
