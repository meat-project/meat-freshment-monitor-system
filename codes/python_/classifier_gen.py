 #相關函式庫
import pandas as pd 
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pickle

df = pd.read_excel('../../result/data.xlsm')
sdf = pd.DataFrame(df)
sdf = sdf.drop(['type','time','month','date','start time'], axis = 1);
mean = sdf['CO2'].mean()
sdf.fillna(mean,inplace = True)
X = sdf.drop(['label'], axis = 1);
y = sdf['label']

print("\n ----------  Adaboost Classifier  ----------\n")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3,random_state = 5)
abc = AdaBoostClassifier(n_estimators = 100, learning_rate = 1)
model = abc.fit(X_train, y_train)
y_pred = abc.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("y_test:",list(y_test))
print("y_pred:",list(y_pred),"\n")

##save module
with open('AdaboostClassifier.pickle','wb') as f:
     pickle.dump(abc, f)
    
print("\n ----------  Bayesian Classifier  ----------\n")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3,random_state = 18)
abc = GaussianNB()
abc.fit(X_train,y_train)
y_pred = abc.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("y_test:",list(y_test))
print("y_pred:",list(y_pred),"\n")

##save module
with open('BayesianClassifier.pickle','wb') as f:
     pickle.dump(abc, f)

print("\n ----------  KNN  ----------\n")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3,random_state = 8)
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train,y_train)
y_pred = neigh.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("y_test:",list(y_test))
print("y_pred:",list(y_pred))

##save module
with open('KNN.pickle','wb') as f:
     pickle.dump(abc, f)


print("\n ----------  DecisionTreeClassifier ---------- \n")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3,random_state = 18)
clf = tree.DecisionTreeClassifier(criterion='gini',random_state=0, max_depth=2)
clf.fit(X, y)
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("y_test:",list(y_test))
print("y_pred:",list(y_pred))

##save module
with open('DecisionTreeClassifier.pickle','wb') as f:
     pickle.dump(clf, f)