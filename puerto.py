# Importamos la libreria de PySerial
import serial
# Abrimos el puerto del arduino a 115200
PuertoSerie = serial.Serial("COM3", 115200)
# Creamos un buble sin fin
while True:
  # leemos hasta que encontarmos el final de linea
  sArduino = PuertoSerie.readline()
  escribir= sArduino.decode('UTF-8')
  print(escribir)