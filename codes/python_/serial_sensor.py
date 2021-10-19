import serial
import string
import time
import pickle
#opening serial port
ser=serial.Serial('/dev/ttyACM0', 9600)

while True:
	serialdata = ser.readline()
	print(serialdata.decode('utf-8'), end='')
	with open('../../result/realtime_sensor_out.txt', 'a') as f:
		f.write(serialdata.decode('utf-8'))

#AdaboostClassifier
"""pickle_in = open('AdaboostClassifier.pickle','rb')
clf = pickle.load(pickle_in)
predict_result = clf.predict(X_predict)"""
#BayesianClassifier.pickle
"""pickle_in = open('BayesianClassifier.pickle','rb')
clf = pickle.load(pickle_in)
predict_result = clf.predict(X_predict)"""
#KNN
"""pickle_in = open('KNN.pickle','rb')
clf = pickle.load(pickle_in)
predict_result = clf.predict(X_predict)"""
