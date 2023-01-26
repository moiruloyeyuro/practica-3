# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 12:30:20 2022

@author: MOISES
"""


import numpy as np
import random
import serial
import time
import matplotlib.pyplot as plt


# ESP32
puerto = "COM3"                  
baud = 115200                      
PuertoSerie = serial.Serial(puerto, baud)
datos=[]
printeados = 0
basura = 0
sumaX = 0
sumaY = 0
sumaZ = 0
X = np.zeros((10),float )
Y=np.zeros((10), float)
Z=np.zeros((10), float)
tiempo=[1,2,3,4,5,6,7,8,9,10]
plt.ion()
figure, ax = plt.subplots(figsize=(8,6))
line1, = ax.plot(tiempo, X)
line2, = ax.plot(tiempo, Y)
line3, = ax.plot(tiempo, Z)

#Lecturas
while basura<10:
        salida = PuertoSerie.readline()       # devuelve un número binario
        salida = salida.decode("UTF-8") # cast de binario a string
        # print(salida)
        basura = basura + 1
        
for printeados in range (10):        
        salida = PuertoSerie.readline()       # devuelve un número binario
        salida = salida.decode("UTF-8") # cast de binario a string

        datos.append(salida)
        a,b,c= datos[printeados].split(";")
        X[printeados]=float(a)
        Y[printeados]=float(b)
        Z[printeados]=float(c)
        plt.plot(tiempo[printeados],X[printeados])
        plt.plot(tiempo[printeados],Y[printeados])
        plt.plot(tiempo[printeados],Z[printeados])
        line1.set_xdata(tiempo)
        line1.set_ydata(X)
        line2.set_xdata(tiempo)
        line2.set_ydata(Y)
        line3.set_xdata(tiempo)
        line3.set_ydata(Z)
        figure.canvas.draw()
    
        figure.canvas.flush_events()
        plt.show()
        sumaX=sumaX+X[printeados]
        sumaY=sumaY+Y[printeados]
        sumaZ=sumaZ+Z[printeados]
        printeados = printeados + 1
mediaX=sumaX/(printeados+1)
mediaY=sumaY/(printeados+1)
mediaZ=sumaZ/(printeados+1)
desviacionX=np.std(X)
desviacionY=np.std(Y)
desviacionZ=np.std(Z) 
print("Media X: ", mediaX)
print("Media Y: ", mediaY)
print("Media Z: ", mediaZ)
print("Desviacion X: ", desviacionX)
print("Desviacion Y: ", desviacionY)   
print("Desviacion Z: ", desviacionZ)      
PuertoSerie.close()