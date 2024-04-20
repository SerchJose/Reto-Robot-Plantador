from customtkinter import *
from PIL import ImageTk, Image #Importasr libreria para imagenes
from tkinter import *

#Configuraciones globales de la UI
set_appearance_mode("System")  # Modes: system (default), light, dark
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Definir Ventana
app = CTk()
app.title("MyanSpace | Robot plantador")
app.geometry("800x500")
# app.minsize(500, 500) # Tamaño minimo de la ventana
# ventana.resizable(0,0) # Bloquear redimensionar ventana manual

# logo = CTkImage(
#             # light_image=Image.open('./Imagenes/f2.jpeg'), # Imagen modo claro
#             dark_image=Image.open('./Imagenes/LoginFondo.webp') # Imagen modo oscuro
#             # size=(800, 500)# Tamaño de las imágenes
# )

bg = PhotoImage(file='./Imagenes/f4.png')
   
# Crear un Canvas
canvas = CTkCanvas(app, width=800, height=500)
canvas.pack(fill="both", expand=True)

# # Poner imagen en el canvas
canvas.create_image(0,0, image=bg, anchor="nw")        

# # Etiqueta para mostrar la imagen
# etiqueta = CTkLabel(master=app, image=logo, text="")
# etiqueta.place(relheight=1, relwidth=1)

# # btn = CTkButton(master=app, text="CTkButton", corner_radius=10, hover_color="black", fg_color="transparent")
# # btn.place(relx=0.5, rely=0.5, anchor="center")

# btn = CTkButton(master=app, text="Iniciar", corner_radius=10, hover_color="grey", fg_color="transparent", bg_color="transparent")
# btn.pack(pady=100)

# # Campos de texto
# # Usuario
# CTkLabel(app, text="Usuario").pack()
# usuario = CTkEntry(app)
# usuario.insert(0, "Nombre de usuario")
# usuario.bind("<Button-1>", lambda e: usuario.delete(0, 'end'))
# usuario.pack()

# # Contraseña
# CTkLabel(app, text="Contraseña").pack()
# contrasena = CTkEntry(app)
# contrasena.insert(0, "*******")
# contrasena.bind("<Button-1>", lambda e: contrasena.delete(0, 'end'))
# contrasena.pack()


# # Menu
# menu = Menu(ventana) # Crear un menu dentro de "ventana"

# ventana.config(menu=menu) # Cargar el menu a la ventana

# archivo = Menu(menu, tearoff=0) # Crear un menu dentro de "mi_menu"
# archivo.add_command(label="Nuevo") # Añadir elementos al menu "archivo"
# archivo.add_command(label="Abrir")
# archivo.add_separator() # Añadir un separador dentro del menu "archivo"
# archivo.add_command(label="Guardar")
# archivo.add_command(label="Guardar Como")
# archivo.add_separator()
# archivo.add_command(label="Salir", command=ventana.quit) # "command=ventana.quit" es para cerrar la ventana

# mi_menu.add_cascade(label="Archivo", menu=archivo) # Añadir elementos de menu desplegables a "mi_menu"
# mi_menu.add_command(label="Editar") # Añadir un elemento al menu "mi_menu"
# mi_menu.add_command(label="Seleccionar")

# Cargar Ventana
app.mainloop()

