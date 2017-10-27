# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 17:00:31 2017
@author: Alvaro
"""

import codecs
import sklearn.neighbors
import sys
import matplotlib.pyplot as plt
import numpy

def plotdata(cases,labels,name): #def function plotdata
#colors = ['black']
    fig, ax = plt.subplots()
    plt.scatter([row[0] for row in cases], [row[1] for row in cases], c=labels)
    ax.grid(True)
    fig.tight_layout()
    plt.title(name)
    plt.xlim(-1, 1.5)
    plt.ylim(-1, 1.5)
    plt.show()


# 0. load and plot data (datos.csv)
# load data
import loaddata
cases = loaddata.load_data()

### 1. Normalization of the data
from sklearn.decomposition import PCA
from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
norm_cases = min_max_scaler.fit_transform(cases)

#2. PCA Estimation
estimator = PCA (n_components = 2)
X_pca = estimator.fit_transform(norm_cases)
print(estimator.explained_variance_ratio_)
labels = [0 for x in range(len(cases))]
#plotdata(X_pca,labels,'basic')


# 3. setting parameters
k = 3
init = "k-means++"
iterations = 20 #  run 10 times with different random centroids
max_iter = 300 # maximum number of iterations for each single run
tol = 1e-04 # controls the tolerance with regard to the changes in the within-cluster sum-squared-error to declare convergence
random_state = 0 # random
# 4. Execute clustering
from scipy import cluster
from sklearn.cluster import KMeans
km = KMeans(k, init, n_init = iterations ,max_iter= max_iter, tol = tol,random_state = random_state)
labels = km.fit_predict(norm_cases)

### 5. Plot the results
plotdata(X_pca,labels, init)


import codecs

import sys
import matplotlib.pyplot as plt
import numpy

from scipy import cluster
from sklearn import preprocessing 
import sklearn.neighbors
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn import metrics
silhouettes = []

for i in range(2, 14):
    km = KMeans(i, init, n_init = iterations ,max_iter= max_iter, tol = tol,random_state = random_state)
    labels = km.fit_predict(norm_cases)
    silhouettes.append(metrics.silhouette_score(norm_cases, labels))


# Plot Silhouette
plt.plot(range(2,14), silhouettes , marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette')
plt.show()
