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
	while serialdata == '' or serialdata.split()[0] != 'H2S:':
		serialdata = ser.readline().decode('utf-8')
	print(serialdata.split()[1])
	ret['H2S'] = serialdata.split()[1]
	serialdata = ser.readline().decode('utf-8')
	print(serialdata.split()[1])
	ret['NH3'] = serialdata.split()[1]
	serialdata = ser.readline().decode('utf-8')
	print(serialdata.split()[1])
	ret['CO2'] = serialdata.split()[1]
	return ret
	

while True:
	dic = getPredictX()
	X_predict = pd.DataFrame(dic)
	print(X_predict)

	'''#AdaboostClassifier
	pickle_in = open('AdaboostClassifier.pickle','rb')
	clf = pickle.load(pickle_in)
	predict_result = clf.predict(X_predict)
	#BayesianClassifier.pickle
	pickle_in = open('BayesianClassifier.pickle','rb')
	clf = pickle.load(pickle_in)
	predict_result = clf.predict(X_predict)
	#KNN
	pickle_in = open('KNN.pickle','rb')
	clf = pickle.load(pickle_in)
	predict_result = clf.predict(X_predict)
	#decisiontree
	pickle_in = open('DecisionTreeClassifier.pickle','rb')
	clf = pickle.load(pickle_in)
	predict_result = clf.predict(X_predict)'''