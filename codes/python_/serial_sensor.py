import serial
import string
import time
#opening serial port
ser=serial.Serial('/dev/ttyACM0', 9600)

while True:
	serialdata = ser.readline()
	print(serialdata.decode('utf-8'), end='')
	with open('../../result/testout.txt', 'a') as f:
		f.write(serialdata.decode('utf-8'))
