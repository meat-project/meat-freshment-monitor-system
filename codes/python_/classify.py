import serial
import string
import time
import pickle
import pandas as pd

#opening serial port
ser=serial.Serial('/dev/ttyACM0', 9600)

def getPredictX():
	serialdata = ''
	ret = {}
	while serialdata.split() == [] or serialdata.split()[0] != 'H2S:': # sometimes there's a bug "out of range...". Add `print('',end='')` can fix it.
		serialdata = ser.readline().decode('utf-8')
	print('H2S: ', serialdata.split()[1], ' ppm')
	ret['H2S'] = float(serialdata.split()[1])
	serialdata = ser.readline().decode('utf-8')
	print('NH3: ', serialdata.split()[1], ' ppm')
	ret['NH3'] = float(serialdata.split()[1])
	serialdata = ser.readline().decode('utf-8')
	print('CO2: ', serialdata.split()[1], ' ppm')
	ret['CO2'] = float(serialdata.split()[1])
	return ret
	

while True:
	dic = getPredictX()
	#print(dic)
	X_predict = pd.DataFrame([dic])
	#print(X_predict)

	#AdaboostClassifier
	pickle_in = open('AdaboostClassifier.pickle','rb')
	clf = pickle.load(pickle_in)
	predict_result = clf.predict(X_predict)
	print("adaboost: \n", predict_result)
	#BayesianClassifier.pickle
	pickle_in = open('BayesianClassifier.pickle','rb')
	clf = pickle.load(pickle_in)
	predict_result = clf.predict(X_predict)
	print("BayesianClassifier: \n", predict_result)
	#KNN
	pickle_in = open('KNN.pickle','rb')
	clf = pickle.load(pickle_in)
	predict_result = clf.predict(X_predict)
	print("KNN: \n", predict_result)
	#decisiontree
	pickle_in = open('DecisionTreeClassifier.pickle','rb')
	clf = pickle.load(pickle_in)
	predict_result = clf.predict(X_predict)
	print("decisiontree: \n", predict_result)
