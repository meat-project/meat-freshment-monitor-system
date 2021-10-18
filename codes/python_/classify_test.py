#相關函式庫
import pandas as pd 
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics

df = pd.read_excel('../../result/data.xlsm')
sdf = pd.DataFrame(df)
sdf = sdf.drop(['type','time','month','date','start time'], axis = 1);
mean = sdf['CO2'].mean()
sdf.fillna(mean,inplace = True)
X = sdf.drop(['label'], axis = 1);
y = sdf['label']

print("\n ----------  Adaboost Classifier  ----------\n")

for i in range(20):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3,random_state = i)
    print("seed:",i)
    abc = AdaBoostClassifier(n_estimators = 100, learning_rate = 1)
    model = abc.fit(X_train, y_train)
    y_pred = abc.predict(X_test)
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    print("y_test:",list(y_test))
    print("y_pred:",list(y_pred),"\n")
    
print("\n ----------  Bayesian Classifier  ----------\n")

for i in range(20):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3,random_state = i)
    print("seed:",i)
    abc = GaussianNB()
    abc.fit(X_train,y_train)
    y_pred = abc.predict(X_test)
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    print("y_test:",list(y_test))
    print("y_pred:",list(y_pred),"\n")