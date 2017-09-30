# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 17:35:44 2015

@author: FranciscoP.Romero
"""
import codecs
import matplotlib.pyplot as plt
import numpy
from sklearn.decomposition import PCA
from sklearn import preprocessing 

# 0. Load Data
f = codecs.open("2009pivot.csv", "r", "utf-8")
states = []
count = 0
for line in f:
	if count > 0: 
		# remove double quotes
		row = line.replace ('"', '').split(",")
		row.pop(0)
		if row != []:
			data = [int(el) for el in row]
			states.append(data)
	count += 1

#1. Normalization of the data (la mas importante)
min_max_scaler = preprocessing.MinMaxScaler()
states = min_max_scaler.fit_transform(states)
       
#2. PCA Estimation
estimator = PCA (n_components = 2)
X_pca = estimator.fit_transform(states)

print(estimator.explained_variance_ratio_) 

#3.  plot (17 dimensiones en gráfico de 2 dim)
numbers = numpy.arange(len(X_pca))
fig, ax = plt.subplots()
for i in range(len(X_pca)):
    plt.text(X_pca[i][0], X_pca[i][1], numbers[i]) 
plt.xlim(-1, 4)
plt.ylim(-0.2, 1)
ax.grid(True)
fig.tight_layout()
plt.show()

