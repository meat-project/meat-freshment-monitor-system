import serial
import string
import time
#opening serial port
ser=serial.Serial('/dev/ttyACM0', 9600)

while True:
	serialdata=ser.readline() 
	print(serialdata)