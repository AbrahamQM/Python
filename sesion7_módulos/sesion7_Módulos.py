# Módulos: ejecutando módulos como scripts

#Sólo son esos archivos.py que hemos ido creando y,
# que se pueden ejecutar con (doble click)
# o ejecutándolo desde la consola con python nombre.py

# Para hacer código limpio se suele hacer así:
#***************************************
#def main():
#   Código principal del programa
#
#def suma(x, y):
#   return x + y
#
#if __name__ == '__main__':
#   main()
#****************************************

# De forma que se ejecute el código solo si es el módulo principal ej:

def main():
  print("Hola desde el main()")


if __name__ == '__main__':
  main()



