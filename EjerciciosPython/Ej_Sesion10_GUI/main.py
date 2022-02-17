# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y
# que contenga un botón de reinicio para que deje todo como al principio.
#
# Al principio no tiene que haber una opción seleccionada.
import tkinter
from tkinter import ttk


def main():
    window = tkinter.Tk()

    window.columnconfigure(0, weight=1)  # weight es el nº de elementos que va a contener
    window.columnconfigure(1, weight=5)
    window.columnconfigure(2, weight=1)

    frame = ttk.Frame(window)
    frame['relief'] = 'sunken'

    label = ttk.Label(frame, text='Seleccione su color')
    label.grid(column=0, row=0, sticky=tkinter.N)

    frame.grid(column=0, row=0, sticky=tkinter.N)

    selected = tkinter.StringVar()

    verde = ttk.Radiobutton(window, text='verde', value='v', variable=selected)
    rojo = ttk.Radiobutton(window, text='rojo', value='r', variable=selected)
    azul = ttk.Radiobutton(window, text='azul', value='b', variable=selected)
    amarillo = ttk.Radiobutton(window, text='amarillo', value='y', variable=selected)
    negro = ttk.Radiobutton(window, text='negro', value='k', variable=selected)

    verde.grid(column=0, row=1, sticky=tkinter.N, padx=30, pady=30)
    rojo.grid(column=1, row=1, sticky=tkinter.N, padx=30, pady=30)
    azul.grid(column=2, row=1, sticky=tkinter.N, padx=30, pady=30)
    amarillo.grid(column=3, row=1, sticky=tkinter.N, padx=30, pady=30)
    negro.grid(column=4, row=1, sticky=tkinter.N, padx=30, pady=30)

    def reiniciar():
        print("Ha reiniciado")
        selected.initialize(tkinter.StringVar())

    reset_button = ttk.Button(window, text='REINICIO', command=reiniciar)
    reset_button.grid(column=2, row=3, sticky=tkinter.N, padx=50, pady=50)

    window.mainloop()


if __name__ == '__main__':
    main()
