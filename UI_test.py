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
    app.geometry("500x300+560+240")
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
                    fg_color="transparent", border_width=1, border_color="white", bg_color="transparent", 
                    width=25, height=30, command=v2)
    btn2 = CTkButton(app, text="Salir", corner_radius=10, hover_color="grey", 
                    fg_color="transparent", border_width=1, border_color="white", bg_color="transparent", 
                    width=25, height=30, command=app.destroy)
    btn1_w = canvas.create_window(225, 250, anchor="nw", window=btn1)
    btn2_w = canvas.create_window(325, 250, anchor="nw", window=btn2)
    # Cargar Ventana
    app.mainloop()

# Segunda ventana
def v2():
    app.withdraw()
    global v2
    v2=CTkToplevel(app)
    v2.title("Tipo de control")
    v2.geometry("500x300+560+240")
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
                 fg_color="transparent", border_width=2, border_color="white", bg_color="transparent", command=manual)
    btn2 = CTkButton(v2, text="Modo Automático", corner_radius=10, hover_color="grey",       
                 fg_color="transparent", border_width=2, border_color="white", bg_color="transparent", command=auto)
    btn3 = CTkButton(v2, text="Salir", border_width=2, border_color="white", command=app.destroy)
    
    btn1_w = canvas1.create_window(125, 200, anchor="nw", window=btn1)
    btn2_w = canvas1.create_window(325, 200, anchor="nw", window=btn2)
    btn3_w = canvas1.create_window(220, 250, anchor="nw", window=btn3)
    
    # if v2():
    #     auto.withdraw()
    #     manual.withdraw()
    
    v2.mainloop()

def manual():
    v2.withdraw()
    global manual
    global v3
    v3=CTkToplevel(v2)
    v3.title("Modo Manual")
    v3.geometry("1000x500+560+240")
    v3.resizable(0,0)
    
    # v3.grid_columnconfigure(0, weight=1)
    
    mapaig = CTkImage(
                light_image = im.open('./Imagenes/map.png'), # Imagen modo claro
                dark_image = im.open('./Imagenes/map.png'), # Imagen modo oscuro 
                size=(300, 300)) # Tamaño de la imagen
    
    move = CTkLabel(v3, text="Mover")
    move.grid(row=0, column=1, sticky="w")
    
    
    btn1 = CTkButton(v3, text="Actuador", corner_radius=10, hover_color="grey", 
                 fg_color="#2195B1", border_width=1, border_color="blue", bg_color="transparent", command=actuador)
    btn1.grid(row=0, column=2, rowspan=2, sticky="nswe")
    
    btn2 = CTkButton(v3, text="Brazo", corner_radius=10, hover_color="grey",       
                 fg_color="#2195B1", border_width=1, border_color="blue", bg_color="transparent", command=brazo)
    btn2.grid(row=2, column=2, rowspan=2, sticky="nswe")
    
    btn3 = CTkButton(v3, text="Back", border_width=1, border_color="white", command=volver)
    btn3.grid(row=0, column=3, rowspan=4, sticky="nswe")
    
    mapa = CTkLabel(v3, image=mapaig, text="")
    mapa.grid(row=0, column=0, rowspan=4, sticky="nswe")
    
    frame1 = CTkFrame(v3)
    frame1.grid(row=1, column=1, rowspan=3, sticky="nswe")
    
    x = CTkLabel(frame1, text="X:")
    x.grid(row=0, column=0,padx=30, pady=10, sticky="e")
    y = CTkLabel(frame1, text="Y:")
    y.grid(row=1, column=0,padx=30, pady=10, sticky="e")
    vel = CTkLabel(frame1, text="Velocidad:")
    vel.grid(row=2, column=0,padx=30, pady=10, sticky="e")
    
    xe = CTkEntry(frame1, placeholder_text="m")
    xe.grid(row=0, column=1,padx=10, pady=10, sticky="e")
    ye = CTkEntry(frame1, placeholder_text="m")
    ye.grid(row=1, column=1,padx=10, pady=10, sticky="e")
    vele = CTkEntry(frame1, placeholder_text="cm/s")
    vele.grid(row=2, column=1,padx=10, pady=10, sticky="e")
    
    # Expandir horizontalmente las columnas
    v3.columnconfigure(1, weight=4)
    v3.columnconfigure(0, weight=1)
    v3.columnconfigure((2,3), weight=2)
    # Expandir verticalmente las filas
    v3.rowconfigure((0,1,2,3), weight=1)
    
    v3.mainloop()
    
def auto():
    v2.withdraw()
    global auto
    global v4
    v4=CTkToplevel(v2)
    v4.title("Modo automatico")
    v4.geometry("1000x300+560+240")
    v4.resizable(0,0)
    
    mapaig = CTkImage(
                light_image = im.open('./Imagenes/map.png'), # Imagen modo claro
                dark_image = im.open('./Imagenes/map.png'), # Imagen modo oscuro 
                size=(250, 200)) # Tamaño de la imagen
    roboig = CTkImage(
                light_image = im.open('./Imagenes/fruit.png'), # Imagen modo claro
                dark_image = im.open('./Imagenes/fruit.png'), # Imagen modo oscuro 
                size=(250, 200)) # Tamaño de la imagen

    # frame1 = CTkFrame(v4)
    # frame1.grid(row=0, column=0, sticky="nswe")
    # frame2 = CTkFrame(v4)
    # frame2.grid(row=0, column=1, sticky="nswe")
    # frame3 = CTkFrame(v4)
    # frame3.grid(row=0, column=2, sticky="nswe")
    
    mapa = CTkLabel(v4, image=mapaig, text="")
    mapa.grid(row=0, column=0,padx=50, pady=10, sticky="nswe")
    mapat = CTkLabel(v4, text="INFORMACIÓN 1")
    mapat.grid(row=1, column=0,padx=50, pady=10, sticky="nswe")
    
    robo = CTkLabel(v4, image=roboig, text="")
    robo.grid(row=0, column=1,padx=50, pady=10, sticky="nswe")
    robot = CTkLabel(v4, text="INFORMACIÓN 2")
    robot.grid(row=1, column=1,padx=50, pady=10, sticky="nswe")
    
    btn3 = CTkButton(v4, text="Back", border_width=1, border_color="white", command=volver1)
    btn3.grid(row=1, column=2,padx=50, pady=10, sticky="ns")
    
    inf = CTkLabel(v4, text="INFORMACIÓN")
    inf.grid(row=0, column=2, padx=50, pady=10, sticky="ns")

    # Expandir horizontalmente las columnas
    v4.columnconfigure((0,1,2), weight=1)
    # Expandir verticalmente las filas
    # v4.rowconfigure((0,1,2,3), weight=1)

    v4.mainloop()

def actuador():
    v3.withdraw()
    global actuador
    global v5
    v5=CTkToplevel(v3)
    v5.title("Actuador sembrador")
    v5.geometry("800x400+560+240")
    v5.resizable(0,0)
    
    mapaig = CTkImage(
                light_image = im.open('./Imagenes/map.png'), # Imagen modo claro
                dark_image = im.open('./Imagenes/map.png'), # Imagen modo oscuro 
                size=(250, 200)) # Tamaño de la imagen
    # roboig = CTkImage(
    #             light_image = im.open('./Imagenes/fruit.png'), # Imagen modo claro
    #             dark_image = im.open('./Imagenes/fruit.png'), # Imagen modo oscuro 
    #             size=(250, 200)) # Tamaño de la imagen

    frame1 = CTkFrame(v5)
    frame1.grid(row=2, column=0, sticky="nswe")
    frame2 = CTkFrame(v5)
    frame2.grid(row=2, column=1, sticky="nswe")
    # frame3 = CTkFrame(v4)
    # frame3.grid(row=0, column=2, sticky="nswe")
    
    mapa = CTkLabel(v5, image=mapaig, text="")
    mapa.grid(row=0, column=0, columnspan=2, padx=50, pady=10, sticky="nswe")
    
    btn1 = CTkButton(v5, text="Plantar", border_width=1, border_color="white")
    btn1.grid(row=1, column=0, padx=50, pady=10, sticky="ns")
    btn2 = CTkButton(v5, text="Retraer", border_width=1, border_color="white")
    btn2.grid(row=1, column=1, padx=50, pady=10, sticky="ns")
    
    sem = CTkLabel(frame1, text="Semillas Plantadas: ")
    sem.grid(row=0, column=0,padx=50, pady=10, sticky="nswe")
    sem1 = CTkLabel(frame1, text="10")
    sem1.grid(row=0, column=1,padx=50, pady=10, sticky="nswe")

    sem2 = CTkLabel(frame2, text="Semillas Almacenadas: ")
    sem2.grid(row=0, column=0,padx=50, pady=10, sticky="nswe")
    sem3 = CTkLabel(frame2, text="8")
    sem3.grid(row=0, column=1,padx=50, pady=10, sticky="nswe")
    
    btn3 = CTkButton(v5, text="Back", border_width=1, border_color="white", command=volver2)
    btn3.grid(row=3, column=0, columnspan=2, padx=50, pady=10, sticky="nswe")

    # Expandir horizontalmente las columnas
    v5.columnconfigure((0,1,2), weight=1)
    # Expandir verticalmente las filas
    # v4.rowconfigure((0,1,2,3), weight=1)

    v5.mainloop()

def brazo():
    v3.withdraw()
    global brazo
    global v6
    v6=CTkToplevel(v3)
    v6.title("Brazo Robótico")
    v6.geometry("800x350+560+240")
    # v6.resizable(0,0)
    
    # mapaig = CTkImage(
    #             light_image = im.open('./Imagenes/map.png'), # Imagen modo claro
    #             dark_image = im.open('./Imagenes/map.png'), # Imagen modo oscuro 
    #             size=(250, 200)) # Tamaño de la imagen
    roboig = CTkImage(
                light_image = im.open('./Imagenes/fruit.png'), # Imagen modo claro
                dark_image = im.open('./Imagenes/fruit.png'), # Imagen modo oscuro 
                size=(250, 200)) # Tamaño de la imagen

    # frame1 = CTkFrame(v6)
    # frame1.grid(row=2, column=0, sticky="nswe")
    # frame2 = CTkFrame(v6)
    # frame2.grid(row=2, column=1, sticky="nswe")
    # frame3 = CTkFrame(v4)
    # frame3.grid(row=0, column=2, sticky="nswe")
    
    robo = CTkLabel(v6, image=roboig, text="")
    robo.grid(row=0, column=0, padx=50, pady=10, sticky="nswe")
    
    btn1 = CTkButton(v6, text="Abrir", border_width=1, border_color="white")
    btn1.grid(row=1, column=0, padx=50, pady=10, sticky="ns")
    btn2 = CTkButton(v6, text="Cerrar", border_width=1, border_color="white")
    btn2.grid(row=1, column=1, padx=50, pady=10, sticky="ns")
    
    info = CTkLabel(v6, text="INFORMACIÓN")
    info.grid(row=0, column=1, padx=50, pady=10, sticky="nswe")
    
    btn3 = CTkButton(v6, text="Back", border_width=1, border_color="white", command=volver3)
    btn3.grid(row=2, column=0, columnspan=2, padx=50, pady=10, sticky="nswe")

    # Expandir horizontalmente las columnas
    v6.columnconfigure((0,1,2), weight=1)
    # Expandir verticalmente las filas
    # v4.rowconfigure((0,1,2,3), weight=1)

    v6.mainloop()

def volver():
    v2.iconify()
    v2.deiconify()
    v3.destroy()
    
def volver1():
    v2.iconify()
    v2.deiconify()
    v4.destroy()

def volver2():
    v3.iconify()
    v3.deiconify()
    v5.destroy()

def volver3():
    v3.iconify()
    v3.deiconify()
    v6.destroy()

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

