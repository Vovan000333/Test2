import pandas as pd
pd.options.mode.chained_assignment = None
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from pip._internal.self_outdated_check import _self_version_check_logic
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from pylab import rcParams
rcParams['figure.figsize'] = 15, 15

dataset = pd.read_csv("./titanic.csv")
dataset = dataset.iloc[0:,[2,4,5,1]]

dataset.loc[dataset["Sex"] == "male", "Sex"] = 0
dataset.loc[dataset["Sex"] == "female", "Sex"] = 1
dataset = dataset.dropna() #Избавились от NAN, потому что не умеет считать
# print(dataset)

dataset_new = dataset.dropna()
ds = dataset_new.iloc[:600,:]
ds_test = dataset_new.iloc[600:,:]
X_train = ds.drop("Survived", axis='columns')
X_test = ds_test.drop("Survived", axis='columns')
Y_train = ds["Survived"]
# print(X_train)
# print(Y_train)
# print(ds)

"""Логистическая модель"""
# logreg = LogisticRegression()
# logreg.fit(X_train, Y_train)
# Y_pred = logreg.predict(X_test)
# acc_log = round(logreg.score(X_train, Y_train) * 100, 4)
# print(acc_log)

# logreg = LogisticRegression()
# logreg.fit(X_train, Y_train)
# Y_pred = logreg.predict(X_test)
# ds_test['predicted'] = Y_pred.tolist()
# ds_test.loc[ds_test["Survived"] == ds_test["predicted"], "Nice"] = 1
# ds_test.loc[ds_test["Survived"] != ds_test["predicted"], "Nice"] = 0
# a = ds_test["Nice"].sum()
# b = ds_test["Nice"].size
# print(a)
# print(b)
# print(a/b)

"""Персептрон"""
perceptron = Perceptron()
perceptron.fit(X_train, Y_train)
Y_pred = perceptron.predict(X_test)
ds_test['predicted'] = Y_pred.tolist()
ds_test.loc[ds_test["Survived"] == ds_test["predicted"], "Nice"] = 1
ds_test.loc[ds_test["Survived"] != ds_test["predicted"], "Nice"] = 0
a = ds_test["Nice"].sum()
b = ds_test["Nice"].size
print(f'Персептрон. \nСумма совпавших результатов: {int(a)}, вся выборка: {b}, вероятность предсказания: {round(a/b*100, 4)} \n')



"""Машина опорных векторов"""
svc = SVC()
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
ds_test['predicted'] = Y_pred.tolist()
ds_test.loc[ds_test["Survived"] == ds_test["predicted"], "Nice"] = 1
ds_test.loc[ds_test["Survived"] != ds_test["predicted"], "Nice"] = 0
a = ds_test["Nice"].sum()
b = ds_test["Nice"].size
print(f'Машина опорных векторов. \nCумма совпавших результатов: {int(a)}, вся выборка: {b}, вероятность предсказания: {round(a/b*100, 4)}')