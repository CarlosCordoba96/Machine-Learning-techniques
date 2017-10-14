# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 17:00:31 2017

@author: Alvaro
"""


import matplotlib.pyplot as plt
import sklearn.neighbors
import numpy as np


def plotdata(cases,labels,name): #def function plotdata
#colors = ['black']
    fig, ax = plt.subplots()
    plt.scatter([row[0] for row in cases], [row[1] for row in cases], c=labels)
    ax.grid(True)
    fig.tight_layout()
    plt.title(name)
    plt.show()


# 0. load and plot data (datos.csv)
# load data 
import loaddata
cases = loaddata.load_data("Data/iq_2000_2003_pivot.csv")
labels = [0 for x in range(len(cases))]
plotdata(cases,labels,'basic')


# 1. setting parameters
k = 5
init = "k-means++"

# 2. Execute clustering 

import sklearn.cluster
centroids, labels, z =  sklearn.cluster.k_means(cases, k, init)

# 3. Plot the results
plotdata(cases,labels, 'kmeans++')

# 4. Validation
from sklearn import metrics
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(np.asarray(cases), labels))




