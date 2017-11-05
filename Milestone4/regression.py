# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:33:52 2017

@author: FranciscoP.Romero
"""


# 0.1 load data
import pandas as pd
bikes = pd.read_csv('bikes.csv')
bikes.head()


#0.2 Explore Data
# charts from https://machinelearningmastery.com/visualize-machine-learning-data-python-pandas/
import matplotlib.pyplot as plt
plt.rcdefaults()

#0.2.1 Univariate Histograms
# 
bikes.hist()
plt.show()
#0.2.2 Density Plots
bikes.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
plt.show()
#0.2.3 Scatterplot matrix
from pandas.tools.plotting import scatter_matrix
scatter_matrix(bikes)
plt.show()

#0.2.4

# NOTE: Low correlation means there's no linear relationship; 
# it doesn't mean there's no information in the feature that predicts the target.


import numpy as np
from scipy.stats.stats import pearsonr 
corr = [pearsonr(bikes['temperature'], bikes['count'])[0], pearsonr(bikes['humidity'], bikes['count'])[0], 
        pearsonr(bikes['windspeed'], bikes['count'])[0]]

 
features= ('temperature', 'humidity', 'windspeed')
y_pos = np.arange(len(features))
 
plt.bar(y_pos, corr, align='center', alpha=0.5)
plt.xticks(y_pos, features)
plt.ylabel('Correlation')
plt.title('Correlation features vs target')

plt.show()

#1. Build the model
from sklearn.tree import DecisionTreeRegressor

#1.1 Model Parametrization 
# criterion: mse mean squared error, which is equal to variance reduction as feature selection criterion
#splitter: best/random
# max_depth: low value avoid overfitting
regressor = DecisionTreeRegressor(criterion='mse', max_depth=2, random_state=0)
#1.2 Model construction
#regressor.fit(bikes[['temperature', 'humidity', 'windspeed']], bikes['count'])
# one feature predictor
regressor.fit(bikes[['temperature']], bikes['count'])

#2.  Model Visualization
import graphviz 
# Don't forget pip install graphviz
from sklearn.tree import export_graphviz
dot_data = export_graphviz(regressor, out_file='tree.dot', feature_names=features, 
                           filled=True, rounded=True)
graph = graphviz.Source(dot_data)  
graph 

# 2.2 Model Plot
xx = np.array([np.linspace(-5, 40, 100)]).T

plt.figure(figsize=(8,6))
plt.plot(bikes['temperature'], bikes['count'], 'o', label='observation')
plt.plot(xx, regressor.predict(xx), linewidth=4, alpha=.7, label='prediction')
plt.xlabel('temperature')
plt.ylabel('bikes')
plt.legend()
plt.show()


# This visualization is only useful for a model of two predictors

nx = 30
ny = 30
# creating a grid of points
x_temperature = np.linspace(-5, 40, nx)
y_humidity = np.linspace(20, 80, ny)
xx, yy = np.meshgrid(x_temperature, y_humidity)
# evaluating the regresson on all the points
z_bikes = regressor.predict(np.array([xx.flatten(), yy.flatten()]).T)
zz = np.reshape(z_bikes, (nx, ny))


fig = plt.figure(figsize=(8, 8))
# plotting the predictions
plt.pcolormesh(x_temperature, y_humidity, zz, cmap=plt.cm.YlOrRd)
plt.colorbar(label='bikes predicted') # add a colorbar on the right
# plotting also the observations
plt.scatter(bikes['temperature'], bikes['humidity'], s=bikes['count']/25.0, c='g')
# setting the limit for each axis
plt.xlim(np.min(x_temperature), np.max(x_temperature))
plt.ylim(np.min(y_humidity), np.max(y_humidity))
plt.xlabel('temperature')
plt.ylabel('humidity')
plt.show()




# 2.2 Feature Relevances

print 'Feature Relevancies'
list1 = zip(features, regressor.feature_importances_)
from tabulate import tabulate
print tabulate(list1, headers=['Feature', 'Relevance'])




# Compute the max 
mae = []
from sklearn.metrics import mean_absolute_error
for i in range(2, 30):
    regressor = DecisionTreeRegressor(max_depth=i)
    regressor.fit(bikes[['temperature', 'humidity']], bikes['count'])
    pred_values = regressor.predict(bikes[['temperature', 'humidity']])
    maev = mean_absolute_error(bikes['count'],pred_values)
    mae.append(maev)
    
# Plot mae   
plt.plot(range(2,30), mae, marker='o')
plt.xlabel('max_depth')
plt.ylabel('mae')
plt.show()


# CROSS VALIDATION ANALYSIS
from sklearn.cross_validation import cross_val_score

total_scores = []
from sklearn.metrics import mean_absolute_error
for i in range(2, 30):
    regressor = DecisionTreeRegressor(max_depth=i)
    regressor.fit(bikes[['temperature', 'humidity']], bikes['count'])
    scores = -cross_val_score(regressor, bikes[['temperature', 'humidity']],
            bikes['count'], scoring='neg_mean_absolute_error', cv=10)
    total_scores.append(scores.mean())

plt.plot(range(2,30), total_scores, marker='o')
plt.xlabel('max_depth')
plt.ylabel('cv score')
plt.show()    
    








