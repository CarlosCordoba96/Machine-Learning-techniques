# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 17:00:31 2017
@author: Alvaro
"""

import matplotlib.pyplot as plt


def plotdata(cases,labels,name): #def plotdata for each of the representations (k-means, silhouette and distortion)
    fig, ax = plt.subplots()
    plt.scatter([row[0] for row in cases], [row[1] for row in cases], c=labels)
    ax.grid(True)
    fig.tight_layout()
    plt.title(name)
    plt.xlim(-1, 1.5)
    plt.ylim(-1, 1.5)
    plt.show()

# load data
import loaddata
cases = loaddata.load_data()

# 
from sklearn.decomposition import PCA
from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
norm_cases = min_max_scaler.fit_transform(cases)

# Creating the pca representation
estimator = PCA (n_components = 2)
X_pca = estimator.fit_transform(norm_cases)
print(estimator.explained_variance_ratio_)
labels = [0 for x in range(len(cases))]


# Applies k-means with these different attributes
k = 3 #Number of centroids
init = "k-means++" #Method that we are using (k-means++ or random)
iterations = 20 #Number of times that the centroids are moved in the mean of their values
max_iter = 300 #Maximum number of moves(itearions)
tol = 1e-04 # controls the tolerance with regard to the changes in the within-cluster sum-squared-error to declare convergence
random_state = 0 #Random state

# Executing the clustering
from sklearn.cluster import KMeans
km = KMeans(k, init, n_init = iterations ,max_iter= max_iter, tol = tol,random_state = random_state)
labels = km.fit_predict(norm_cases)

# Plots the results: PCA with the centroids, Silhouette coefficient and distortion
plotdata(X_pca,labels, init)

print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(norm_cases, labels))
print('Distortion: %.2f' % km.inertia_)
