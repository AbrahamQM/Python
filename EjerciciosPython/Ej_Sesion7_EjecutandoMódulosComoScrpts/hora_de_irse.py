# En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa.
# Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

# En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario,
# haréis una operación para calcular el tiempo que queda de trabajo.
import time

hora = time.strftime('%H:%M', time.localtime())
print("Son las: ", hora)

if int(hora[:2]) >= 19:
    print("--YA es hora de irse a casa!!!")
else:
    h = int(hora[:2])
    m = int(hora[3:5])
    falta_h = 18 - h
    falta_m = 60 - m
    print(f'Aún no es hora de irse, te quedan {falta_h} H y {falta_m} Min trabajando')
