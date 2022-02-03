
# Programación multi-hilo:
print("Programación multi-Hilo, para ejecutar funciones en paralelo")


import _thread
import time


def horaActual():
    print("\n*Hola desde horaActual()")


print("\n-Usamos : _thread.start_new_thread(horaActual, (parámetros))")
_thread.start_new_thread(horaActual, ())

print("\n!!Cuando se ejecuta código multi-hilo, "
      "tenemos que detener o ralentizar el programa para que se ejecute nuestro código paralelo¡¡¡")
print("\n-Por ejemplo poniendo time.sleep(segundos):\ntime.sleep(1)")

time.sleep(1)


print("\n-Otra forma de hacer esperar al programa es:\nwhile True:\n  time.sleep(0.1)")

print("\n**************************** Ejemplo para ver como se ejecutan en paralelo **********************************")
print('\n**Modifico la función horaActual(nombreThread, TiempoEspera), para que se ejecute de otra forma.(Ver código)')


def horaActual(nombreThread, TiempoEspera):
    count = 0

    while count < 3:
        time.sleep(TiempoEspera)
        count += 1
        print(f'-Hilo: {nombreThread} - {time.ctime(time.time())}')


print("**La ejecuto asi:\n_thread.start_new_thread(horaActual, ('thread_uno', 1))"
      "\n_thread.start_new_thread(horaActual, ('thread_dos', 2))\n\n*Resultado:")
_thread.start_new_thread(horaActual, ("thread_uno", 1))
_thread.start_new_thread(horaActual, ("thread_dos", 2))

print("--Cada hilo se va ejecutando simultáneamente, thread_uno(cada segundo) y thread_dos(cada 2 segundos) "
      "según le indicamos al invocarlos")

while True:
    time.sleep(0.01)

