# GRID es una geometría de tkinter que funciona como una hoja de excel:
# (0,0) (1,0) (2,0) (3,0)
# (0,1) (1,1) (2,1) (3,1)
# (0,2) (1,2) (2,2) (3,2)
# (0,3) (1,3) (2,3) (3,3)

import tkinter
from tkinter import ttk # (Template Toolkit) es una librería de tkinter para darle estilos

window = tkinter.Tk()

window.columnconfigure(0, weight=1)  # weight es el nº de elementos que va a contener
window.columnconfigure(1, weight=3)

# Creamos las etiquetas
username_label = ttk.Label(window, text="Username:")
password_label = ttk.Label(window, text="Password:")


# Posicionamos
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5) # row = fila, sticky = fijar en un sitio
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=2)
# tkinter.W: W es una coordenada(West)


# ************* Input box  o caja de texto ******
username_entry = ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

password_entry = ttk.Entry(window, show='*')  # show para que sólo muestre ese caracter en lugar de la contraseña
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)


#  ************** Botones *******************


login_butto = ttk.Button(window, text='Login')
login_butto.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)






window.mainloop()





