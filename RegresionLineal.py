import matplotlib.pyplot as plt
import pandas as panda
import numpy as num
from sklearn.linear_model import LinearRegression
def regresion():
    ventas = panda.read_csv("datos_ejemplo_regresion_lineal.csv") #Abrimos el archivo de los datos
    objetivo = "monto"
    variables_independientes = ventas.drop(columns=['monto']).columns
    modelo = LinearRegression()
    modelo.fit(ventas[variables_independientes], ventas[objetivo])
    ##modelo.fit(X=ventas[variables_independientes], y=ventas[objetivo])
    ventas["ventas_prediccion"] = modelo.predict(ventas[variables_independientes])
    preds = ventas[["monto", "ventas_prediccion"]].head(100)
    edad_entrada=float(input("Ingresa la edad del chofer ->"))
    kilometraje_entrada=float(input("Ingresa el kilometraje del carro ->"))
    uso=float(input("Ingresa el uso del carro 1 si es particular, 2 si es transporte pÃºblico (Uber, Didi o Taxi)->"))
    medio_pago=float(input("Ingresa el mÃ©todo de pago 1 tarjeta, 2 efectivo, 3 transferencia->"))
    posible_monto = modelo.predict([[edad_entrada,kilometraje_entrada,uso,medio_pago]])
    print ("El monto de compra posiblemente serÃ¡: ",posible_monto)
while 1:
    print("1.-Ejemplo de regresion\n\r9.-Salir")
    opcion=int(input("-> "))
    if opcion==1:
        regresion()
    elif opcion==9:
        print("Que tengas un buen di­a")
        exit()
        break
    else:
        print("Introduce una opcion valida")