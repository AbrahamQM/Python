# En MacOs hay que instalar tkinter, en windows viene con python
# Usa un lenguaje que se llama TCL, y un toolkit llamado TK

# Uso de tcl en python con la librería (tkinter) que adapta TCL a python


# USO de tkinter

import tkinter

import pprint
# Contenedor de ventanas
window = tkinter.Tk()
print(type(window))
pprint.pprint(dir(window))

# Creación de ventanas
print("Hay que crear un bucle para que la ventana se mantenga abierta:\nNombreDeVentana.mainloop()")

# window.mainloop() COMENTADA POR QUE SI SE MUESTRA LA VENTANA NO CARGA LO SIGUIENTE (puesto mas abajo)

# Widget label

label_saludo = tkinter.Label(window, text="Hola!", bg="yellow", fg="blue") # bg = color de fondo, fg= color de la fuente



# Posicionamiento o GEOMETRÍA de elementos (widget)

# Usamos la geometría pack en este caso con pack ipadx(Horizontal), ipady(vertical)
# Con fill, indicamos que se expanda all el espacio de la ventana **Admite como parámetro un string
# (ancho"x", alto"y", ambos "both")

label_saludo.pack(ipadx=30, ipady=30, fill="x")

label_adios = tkinter.Label(window, text="Adios", bg="red", fg="white")
label_adios.pack(ipadx=150, ipady=80, fill="both") # no se expande en la vertical no se por que

label_nombre = tkinter.Label(window, text="nombre", bg="black", fg="grey")
label_nombre.pack(ipadx=30, ipady=50, expand=True) # expand hace que se centre siempre indiferentemente del tamaño

# Posicionamiento
label_dcha = tkinter.Label(window, text="DERECHA", bg='brown', fg="black")
label_dcha.pack(ipadx=30, ipady=30, side='right') # Con side, elegimos donde se posicionará

label_izda = tkinter.Label(window, text="IZQUIERDA", bg='brown', fg="black")
label_izda.pack(ipadx=30, ipady=30, side='left')

label_arriba = tkinter.Label(window, text="Arriba", bg='orange', fg="black")
label_arriba.pack(ipadx=15, ipady=15, side='top')

label_arriba = tkinter.Label(window, text="ABAJO", bg='green', fg="black")
label_arriba.pack(ipadx=45, ipady=20, side='bottom')




window.mainloop()





