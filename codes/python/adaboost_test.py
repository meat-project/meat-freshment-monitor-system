#相關函式庫
import pandas as pd 
import numpy as np
import csv
from sklearn.ensemble import AdaBoostClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics

print("reading..")
df = pd.read_csv('../result/all_fixed.csv')
print(df)
sdf = pd.DataFrame(df)
sdf = sdf.drop(['type','time','month','day'], axis = 1);
mean = sdf['CO2'].mean()
sdf.fillna(mean,inplace = True)
print(sdf)

print("splitting")
X = sdf.drop(['label'], axis = 1);
y = sdf['label']
print(X)
print(y)
        
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)
abc = AdaBoostClassifier(n_estimators = 100, learning_rate = 1)
model = abc.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))