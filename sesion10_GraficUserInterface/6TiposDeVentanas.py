import tkinter
from tkinter import filedialog, colorchooser

window = tkinter.Tk()

# Dos pequeños ejemplos de cuadros de diálogo.

filename = filedialog.askopenfilename()  # Dialogo para abrir fichero
filename2 = colorchooser.askcolor(initialcolor='#ffffff')  # Dialogo para Elegir un color


window.mainloop()

