from tkinter import *
from tkinter import messagebox # Modulo para las alertas
from tkinter import ttk

# Definir Ventana
ventana = Tk()
ventana.title("MyanSpace | Robot plantador")
# ventana.geometry("500x500")
ventana.minsize(500, 500) # Tamaño minimo de la ventana
ventana.resizable(0,0)

# Menu
menu = Menu(ventana) # Crear un menu dentro de "ventana"

ventana.config(menu=menu) # Cargar el menu a la ventana

archivo = Menu(menu, tearoff=0) # Crear un menu dentro de "mi_menu"
archivo.add_command(label="Nuevo") # Añadir elementos al menu "archivo"
archivo.add_command(label="Abrir")
archivo.add_separator() # Añadir un separador dentro del menu "archivo"
archivo.add_command(label="Guardar")
archivo.add_command(label="Guardar Como")
archivo.add_separator()
archivo.add_command(label="Salir", command=ventana.quit) # "command=ventana.quit" es para cerrar la ventana

mi_menu.add_cascade(label="Archivo", menu=archivo) # Añadir elementos de menu desplegables a "mi_menu"
mi_menu.add_command(label="Editar") # Añadir un elemento al menu "mi_menu"
mi_menu.add_command(label="Seleccionar")

# Cargar Ventana
ventana.mainloop()