# -*- coding: utf-8 -*-
"""
Created on Fri Dec 01 12:29:37 2017

@author: Alvaro
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import numpy as np

def loaddata():
    #read sanjuan
    sj = pd.read_csv('Data/sanjuan/dengue_features_train.csv')
    sj2=pd.read_csv('Data/sanjuan/dengue_labels_train.csv')
    sanjuan = pd.merge(sj, sj2, on=['city', 'year','weekofyear'])
    
    sanjuan=sanjuan.drop(sanjuan.index[[88,140,400,452,752,712,764,495]])#principal outliers
    
    sanjuan=sanjuan.drop(sanjuan.index[[700,502,361,253,254,330,493]])
    sanjuan = sanjuan.fillna(sanjuan.mean())#There is some data as NaN
    
    return sanjuan

data=loaddata()
feat = ['weekofyear','reanalysis_dew_point_temp_k','reanalysis_specific_humidity_g_per_kg','station_max_temp_c']
#Parametrization
X = data[feat]
y = data['total_cases']

regressor = RandomForestRegressor(n_estimators= 1000, max_depth = 5, criterion='mae', random_state=0)


####################################
#APLICACION DEL MODEL AL PROPIO TRAINING DATASET
####################################
# sample a training set while holding out 40% of the data for testing (evaluating) our classifier:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

# 2.2 Feature Relevances

#1.1 Model Parametrization 
#regressor = RandomForestRegressor(n_estimators= 10, max_depth = 5, criterion='mae', random_state=0)
#1.2 Model construction
regressor.fit(X_train, y_train)

# Test
y_pred = regressor.predict(X_test)

# metrics calculation 
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test,y_pred)
print "Error Measure ", mae


# x axis for plotting
xx = np.stack(i for i in range(len(y_test)))
#plt.scatter(xx, y_test, c='r', label='data')
plt.plot(xx, y_pred, c='g', label='prediction')
plt.axis('tight')
plt.legend()
plt.title("Gaussian NaiveBayes")

plt.show()

# FEATURE RELEVANCIES
print 'Feature Relevancies'
list1 = zip(feat, regressor.feature_importances_)
from tabulate import tabulate
print tabulate(list1, headers=['Feature', 'Relevance'])
# 2.2 Feature Relevances















#**************************************************************
#TEST: DONT YOU DARE TO TOUCH UNDER THIS LINE
#**************************************************************
#1.1 Model Parametrization 
#regressor = RandomForestRegressor(n_estimators= 10, max_depth = 5, criterion='mae', random_state=0)
#1.2 Model construction
regressor.fit(X, y)

# Test
#read test data
datosTest = pd.read_csv("Data/dengue_features_test_sanjuan.csv")
datosTest=datosTest.fillna(datosTest.mean())
test = datosTest[feat]


# prediction
prediccion = regressor.fit(X,y).predict(test)


# metrics calculation 
#from sklearn.metrics import mean_absolute_error
#mae = mean_absolute_error(y_test,y_pred)
#print "Error Measure ", mae



#plt.subplot(2, 1, i + 1)
#x axis for plotting

xx = np.stack(i for i in range(len(test)))
plt.plot(xx, prediccion, c='g', label='prediction')
plt.axis('tight')
plt.legend()
plt.title("Random Forest")

plt.show()

# FEATURE RELEVANCIES
print 'Feature Relevancies'
list1 = zip(feat, regressor.feature_importances_)
from tabulate import tabulate
print tabulate(list1, headers=['Feature', 'Relevance'])

# PRINTING

datosTest['total_cases']=prediccion

datosTest['total_cases']=datosTest['total_cases'].astype(int)

final=datosTest[['city','year','weekofyear','total_cases']]


final.to_csv('predictedsanjuan.csv',index=False)