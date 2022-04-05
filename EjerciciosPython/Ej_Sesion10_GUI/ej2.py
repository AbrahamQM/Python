# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener
# una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

import tkinter
from tkinter import ttk

def main():
    window = tkinter.Tk()

    window.columnconfigure(0, weight=1)  # weight es el nº de elementos que va a contener
    window.columnconfigure(1, weight=5)
    window.columnconfigure(2, weight=1)

    frame = ttk.Frame(window)
    frame['relief'] = 'sunken'

    label = ttk.Label(frame, text='Elija un animal')
    label.grid(column=0, row=0, sticky=tkinter.N)

    frame.grid(column=0, row=0, sticky=tkinter.N)

    selected = tkinter.StringVar()

    perro = ttk.Radiobutton(window, text='Perro', value='p', variable=selected)
    gato = ttk.Radiobutton(window, text='Gato', value='g', variable=selected)
    elefante = ttk.Radiobutton(window, text='Elefante', value='e', variable=selected)
    delfin = ttk.Radiobutton(window, text='Delfin', value='d', variable=selected)
    aguila = ttk.Radiobutton(window, text='Águila', value='a', variable=selected)

    perro.grid(column=0, row=1, sticky=tkinter.N, padx=30, pady=30)
    gato.grid(column=1, row=1, sticky=tkinter.N, padx=30, pady=30)
    elefante.grid(column=2, row=1, sticky=tkinter.N, padx=30, pady=30)
    delfin.grid(column=3, row=1, sticky=tkinter.N, padx=30, pady=30)
    aguila.grid(column=4, row=1, sticky=tkinter.N, padx=30, pady=30)

    window.mainloop()

if __name__ == '__main__':
    main()



