import serial
import time

# ESP32
puerto = "COM3"                  
baud = 115200                      
PuertoSerie = serial.Serial(puerto, baud)


#Lecturas

printeados = 0

while printeados<10:
        salida = PuertoSerie.readline()       # devuelve un número binario
        salida = salida.decode("UTF-8") # cast de binario a string
        print(salida)
        printeados = printeados + 1
    
PuertoSerie.close()
    