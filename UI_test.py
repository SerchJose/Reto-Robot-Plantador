from customtkinter import *
import PIL.Image as im
import PIL.ImageTk as imtk 
from tkinter import *

#Configuraciones globales de la UI
set_appearance_mode("System")  # Modes: system (default), light, dark
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
set_widget_scaling(1.0)  # widget dimensions and text size
set_window_scaling(1.0)  # window geometry dimensions

# Definir Ventana
def app():
    global app
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
    # Cargar Ventana
    app.mainloop()

# Segunda ventana
def v2():
    app.withdraw()
    global v2
    v2=CTkToplevel(app)
    v2.title("Tipo de control")
    v2.geometry("500x300")
    v2.resizable(0,0)
    
    bg = imtk.PhotoImage(file='./Imagenes/f4.png')
    # Crear un Canvas 
    canvas1 = CTkCanvas(v2, width=800, height=500)
    canvas1.pack(fill="both", expand=True)
    # # Poner imagen en el canvas
    canvas1.create_image(0,0, image=bg, anchor="nw")        
    # Poner una etiqueta
    canvas1.create_text(325, 100, text="Elige un modo para continuar", font=("Helvet", 20), fill="white")
    
    btn1 = CTkButton(v2, text="Modo Manual", corner_radius=10, hover_color="grey", 
                 fg_color="transparent", border_color="white", bg_color="transparent", command=manual)
    btn2 = CTkButton(v2, text="Modo Automático", corner_radius=10, hover_color="grey",       
                 fg_color="transparent", border_color="white", bg_color="transparent", command=auto)
    btn3 = CTkButton(v2, text="Salir", border_color="#FFCC70", command=app.destroy)
    
    btn1_w = canvas1.create_window(125, 200, anchor="nw", window=btn1)
    btn2_w = canvas1.create_window(325, 200, anchor="nw", window=btn2)
    btn3_w = canvas1.create_window(220, 250, anchor="nw", window=btn3)
    
    if v2():
        auto.withdraw()
        manual.withdraw()
    
    v2.mainloop()

def manual():
    v2.withdraw()
    global manual
    v3=CTkToplevel(app)
    v3.title("Tipo de control")
    v3.geometry("500x300")
    v3.resizable(0,0)
    
    bg = imtk.PhotoImage(file='./Imagenes/f4.png')
    # Crear un Canvas 
    canvas1 = CTkCanvas(v3, width=800, height=500)
    canvas1.pack(fill="both", expand=True)
    # # Poner imagen en el canvas
    canvas1.create_image(0,0, image=bg, anchor="nw")  
    mapa = imtk.PhotoImage(file='./Imagenes/map.png')    
    canvas1.create_image(0,0, image=mapa, anchor="nw")  
    # Poner una etiqueta
    # canvas1.create_text(325, 100, text="Elige un modo para continuar", font=("Helvet", 20), fill="white")
    
    # btn1 = CTkButton(v3, text="Modo Manual", corner_radius=10, hover_color="grey", 
    #              fg_color="transparent", border_color="white", bg_color="transparent")
    # btn2 = CTkButton(v3, text="Modo Automático", corner_radius=10, hover_color="grey",       
    #              fg_color="transparent", border_color="white", bg_color="transparent")
    btn3 = CTkButton(v3, text="Back", border_color="#FFCC70", command=volver)
    
    # btn1_w = canvas1.create_window(125, 200, anchor="nw", window=btn1)
    # btn2_w = canvas1.create_window(325, 200, anchor="nw", window=btn2)
    btn3_w = canvas1.create_window(220, 250, anchor="nw", window=btn3)
    
    v3.mainloop()
    
def auto():
    v2.withdraw()
    global auto
    v4=CTkToplevel(app)
    v4.title("Tipo de control")
    v4.geometry("500x300")
    v4.resizable(0,0)
    
    bg = imtk.PhotoImage(file='./Imagenes/f4.png')
    # Crear un Canvas 
    canvas1 = CTkCanvas(v4, width=800, height=500)
    canvas1.pack(fill="both", expand=True)
    # # Poner imagen en el canvas
    canvas1.create_image(0,0, image=bg, anchor="nw")  
    mapa = imtk.PhotoImage(file='./Imagenes/map.png')    
    canvas1.create_image(0,0, image=mapa, anchor="nw")  
    # Poner una etiqueta
    # canvas1.create_text(325, 100, text="Elige un modo para continuar", font=("Helvet", 20), fill="white")
    
    # btn1 = CTkButton(v3, text="Modo Manual", corner_radius=10, hover_color="grey", 
    #              fg_color="transparent", border_color="white", bg_color="transparent")
    # btn2 = CTkButton(v3, text="Modo Automático", corner_radius=10, hover_color="grey",       
    #              fg_color="transparent", border_color="white", bg_color="transparent")
    btn3 = CTkButton(v4, text="Back", border_color="#FFCC70", command=volver1)
    
    # btn1_w = canvas1.create_window(125, 200, anchor="nw", window=btn1)
    # btn2_w = canvas1.create_window(325, 200, anchor="nw", window=btn2)
    btn3_w = canvas1.create_window(220, 250, anchor="nw", window=btn3)

    v4.mainloop()

def volver():
    v2.iconify()
    v2.deiconify()
    v3.destroy()
    
def volver1():
    v2.iconify()
    v2.deiconify()
    v4.destroy()

app()

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

