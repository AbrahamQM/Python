# PLACE es una geometría de tkinter que funciona posicionando de forma absoluta dentro de una ventana, o de forma
# relativa a un elemento dentro de la ventana.
# **Con posicionamiento exacto dándole 'x' e 'y' en pixels

# Se usa en raras ocasiones.

import tkinter
import random

window = tkinter.Tk()


label1 = tkinter.Label(window, text="Posicionamiento absoluto", bg='blue', fg="white")
label1.place(x=10, y=50) # x=separación de la izquierda, y=separación de arriba

label2 = tkinter.Label(window, text="Posicionamiento relativo", bg='red', fg='black')
label2.place(relx=0.10, rely=0.15, relwidth=0.5, anchor='ne')

window.mainloop()

# Ejemplo window2 para jugar con colores y un for colocando etiquetas aleaoriamente
window2 = tkinter.Tk()
colors = ['blue', 'red', 'yellow', 'purple', 'green', 'black']

for x in range(0, 10):
    color = random.randint(0, len(colors)-1)
    color2 = random.randint(0, len(colors)-1)
    ancho = random.randint(0, 200)
    alto = random.randint(0, 500)
    label = tkinter.Label(window2, text='etiqueta!', bg=colors[color], fg=colors[color2])
    label.place(x=ancho, y=alto)


window2.mainloop()

