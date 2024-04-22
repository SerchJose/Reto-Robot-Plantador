from customtkinter import *
import PIL.Image as im
import PIL.ImageTk as imtk 
from tkinter import *

#Configuraciones globales de la UI
set_appearance_mode("System")  # Modes: system (default), light, dark
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
set_widget_scaling(1.0)  # widget dimensions and text size
set_window_scaling(1.0)  # window geometry dimensions

def v2():
    app.withdraw()
    v2=CTkToplevel(app)
    v2.title("Tipo de control")
    v2.geometry("1200x700")
    v2.resizable(0,0)
    btn1 = CTkButton(v2, text="Modo Manual", corner_radius=10, hover_color="grey", 
                 fg_color="transparent", border_color="white", bg_color="transparent")
    btn2 = CTkButton(v2, text="Modo Automático", corner_radius=10, hover_color="grey",       
                 fg_color="transparent", border_color="white", bg_color="transparent")
    
    btn3 = CTkButton(v2, text="Salir", border_color="#FFCC70", command=app.destroy)
    
    btn1.place(relx=0.4, rely=0.3, anchor="center")
    btn2.place(relx=0.6, rely=0.3, anchor="center")
    btn3.place(relx=0.5, rely=0.5, anchor="center")

    v2.mainloop()


# Definir Ventana
app = CTk()
app.title("MyanSpace | Robot plantador")
app.geometry("500x300")
# app.minsize(500, 500) # Tamaño minimo de la ventana
app.resizable(0,0) # Bloquear redimensionar ventana manual

# logo = CTkImage(
#             light_image = PIL.Image.open('./Imagenes/f4.png'), # Imagen modo claro
#             dark_image = PIL.Image.open('./Imagenes/f4.png')) # Imagen modo oscuro

bg = imtk.PhotoImage(file='./Imagenes/f4.png')
   
# Crear un Canvas 
canvas = CTkCanvas(app, width=800, height=500)
canvas.pack(fill="both", expand=True)

# # Poner imagen en el canvas
canvas.create_image(0,0, image=bg, anchor="nw")        

# Poner una etiqueta
canvas.create_text(325, 100, text="MayanSpace Robot", font=("Helvet", 20), fill="white")

#Poner botones
btn1 = CTkButton(app, text="Inicio", corner_radius=10, hover_color="grey", 
                 fg_color="transparent", bg_color="transparent", width=10, height=10, command=v2)
btn2 = CTkButton(app, text="Salir", corner_radius=10, hover_color="grey", 
                 fg_color="transparent", bg_color="transparent", width=15, height=10, command=app.destroy)

btn1_w = canvas.create_window(225, 300, anchor="nw", window=btn1)
btn2_w = canvas.create_window(325, 300, anchor="nw", window=btn2)

#----------------------------------------------------------------

# # Create a function to display other widgets on background 
# def display_widgets(): 
#     # Write some text on the image 
#     canvas.create_text(300, 100, text="MayanSpace Robot", font=("Helvet", 20), fill="white")

# # Función de redimensionar 
# def resizer(e):
#     global bg1, resized_bg, new_bg
#     # Abrir imagen
#     bg1 = im.open('./Imagenes/f4.png')
#     # Call the resize_image function 
#     resized_bg = bg1.resize((e.width, e.height), im.ANTIALIAS)
#     # Definir nueva imagen
#     new_bg = imtk.PhotoImage(resized_bg)
#     # Añadir de nuevo al canvas
#     canvas.create_image(0,0, image=new_bg, anchor="nw")     
#     # Añadir de nuevo el texto
#     display_widgets() 

# # Redimensionar cosas en la ventana
# app.bind('<Configure>', resizer)

# Cargar Ventana
app.mainloop()

