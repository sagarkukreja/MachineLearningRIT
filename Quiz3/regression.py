# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 20:17:26 2018

@author: Sagar
"""

import numpy as np
import numpy as genfromtxt
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn import linear_model
from sklearn.model_selection import KFold
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

X = np.loadtxt('traindata.txt', usecols=range(8))
y = np.loadtxt('traindata.txt',usecols=8)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train.shape, y_train.shape)
print (X_test.shape, y_test.shape)

Y_test_data = np.loadtxt('testinputs.txt',usecols=range(8))

#cross - validation
#for degree in range(8):
model = make_pipeline(PolynomialFeatures(2), linear_model.LinearRegression())
model.fit(X_train, y_train)
Y_test_predict = model.predict(X_test)
error = mean_squared_error(y_test, Y_test_predict)
print(error)
    
Y_new_data_predict = model.predict(Y_test_data)   
np.savetxt("foo.csv", Y_new_data_predict, delimiter=",") 
plt.scatter(y_test, Y_test_predict)


plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.show()