# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener
# una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

import tkinter
from tkinter import *

def main():
    elementos = ['Casa', 'Coche', 'Hijos', 'Mascota', 'Barco', 'Empleo']
    master = Tk()
    lista = StringVar()
    listbox = Listbox(master)
    for item in elementos:
        listbox.insert(END, item)
    listbox.pack()
    label = Label(text="Logros personales:")
    label.pack()
    master.mainloop()

if __name__ == '__main__':
    main()

