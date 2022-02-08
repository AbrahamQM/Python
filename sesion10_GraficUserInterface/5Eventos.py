import tkinter

window = tkinter.Tk()

# Ej1 Click
def funcionClick():
    print("Ha hecho click!!!!!!")

boton = tkinter.Button(window, text='Haz Click', command=funcionClick)
boton.pack()

# Ej2 Click, Doble click y botón secundario
def saludar(event):
    print("Hola, gracias por apretar boton2")


def saludar2(event):
    print("Han hecho doble click")

def saludar3(event):
    print("Click botón derecho")


boton2 = tkinter.Button(window, text="Este es el botón 2")
boton2.pack()
boton2.bind('<Button-1>', saludar)  # <Button-1> es la forma de indicar botón ppal del ratón
boton2.bind('<Double-1>', saludar2)  # <Double-1> es doble click
boton2.bind('<Button-3>', saludar3)  # <Button-3> es boton derecho raton

# Ej3 Botón salir
def salir(event):
    print("Han pulsado SALIR")
    # exit() Sería para cerrar el programa, para cerrar la ventana, usar el siguiente:
    window.quit()


botonSalir = tkinter.Button(window, text="SALIR")
botonSalir.pack()
botonSalir.bind('<Button-1>', salir)



window.mainloop()
# Ver todos los eventos en https://python-course.eu/tkinter/events-and-binds-in-tkinter.php
