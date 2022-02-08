import pprint
# Vamos a trabajar con la geometría de grid, pero se podría hacer con cualquier otra


import tkinter
from tkinter import ttk # (Template Toolkit) es una librería de tkinter para darle estilos

window = tkinter.Tk()

window.columnconfigure(0, weight=1)  # weight es el nº de elementos que va a contener
window.columnconfigure(1, weight=3)
window.columnconfigure(2, weight=3)
window.columnconfigure(3, weight=3)


# ************ Frames o marcos para posicionar objetos ***************************************************************
frame = ttk.Frame(window)  # ancho y alto
frame['relief'] = 'sunken'   # Frame es un diccionario, así que podemos modificarle valores

label = ttk.Label(frame, text='hola')
label.grid(column=0, row=0, sticky=tkinter.N, padx=50, pady=50)

frame.grid(column=0, row=0, sticky=tkinter.W)


# *********** List box, listas de selección **********************************************************************

lista = ['Windows', 'macOs', 'Linux', 'MS DOS', 'amigaOS', 'BeOs', 'OS/2']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=10, listvariable=lista_items) # En esta línea convertimos la lista al
# formato que necesita Listbox
listbox.grid(column=1, row=0, sticky=tkinter.E)

# ************* Radiobutton o botones de selección redondos
selected = tkinter.StringVar()  # Selected será una variable que guardará el resultado de la selección

r1 = ttk.Radiobutton(window, text='Si', value='1', variable=selected)
r2 = ttk.Radiobutton(window, text='No', value='2', variable=selected)
r3 = ttk.Radiobutton(window, text='Puede', value='3', variable=selected)

r1.grid(column=2, row=1, padx=5, pady=5)
r2.grid(column=2, row=2, padx=5, pady=5)
r3.grid(column=2, row=3, padx=5, pady=5)
# Sólo nos dejará marcar una opción por cada variable que le indiquemos ya que todas las opciones tienen esa variable
# en común. Para hacer otro grupo de botones, instanciar una nueva variable


# ************* Check box *******************************************************************************************
def miFuncion():
    print("Ha aceptado las condiciones")


seleccionado = tkinter.StringVar()


checkbox = ttk.Checkbutton(window, text='Acepto las condiciones', variable=seleccionado, command=miFuncion)
# command es otro parámetro que ejecuta una función cuando se realiza la acción correspondiente
checkbox.grid(column=3, row=1, padx=5, pady=5)








window.mainloop()



