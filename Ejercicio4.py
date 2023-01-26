# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 19:55:26 2022

@author: MOISES
"""

import csv
import serial
import time

# ESP32
puerto = "COM3"                  
baud = 115200                      
PuertoSerie = serial.Serial(puerto, baud)
printeados = 0

#Archivo
datos=[]
nombre_archivo ="datos.txt"
with open(nombre_archivo,'w',newline='') as csvFile:
    writer = csv.writer(csvFile,delimiter=';')  
#Lectura


    while printeados<10:   
        salida = PuertoSerie.readline()          # devuelve un número binario
        salida = salida.decode("UTF-8")    # cast de binario a string     
        datos.append(salida) 
        # print(datos)          # añade los elementos salida a la lista datos[]
        a,b,c= datos[printeados].split(";")  # divide la cadena cada vez que ve ';'
        print(a)
        print(b)
        print(c)
        writer.writerow([float(a),float(b),float(c)])                   
        printeados=printeados+1   
 
PuertoSerie.close()
csvFile.close()





