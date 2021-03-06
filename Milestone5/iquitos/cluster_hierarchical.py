# -*- coding: utf-8 -*-

"""
Created on Mon Nov 13 17:44:42 2016
@author: Julián
"""

import matplotlib.pyplot as plt
import numpy
from scipy import cluster
from sklearn import preprocessing 
import sklearn.neighbors
import pandas as pd

# Loads the data into array 'cases'
import loaddata
#cases = loaddata.load_data()
cases=pd.read_csv('Data/dengue_features_train.csv')
 
# Remove outliers that present problems for the initial reading
cases=cases.drop(cases.index[[22,58,94,183,235,274,337,338,365,391,443,465,474,495,496,509]])
cases=cases.drop(cases.index[[101,3,50,300,10,112,268,239,474]])
    
cases=cases.fillna(cases.mean())
print cases
cases.to_csv('out.csv',index=False)
cases=loaddata.load_data()

# Normalization of the data to work with it in clustering
min_max_scaler = preprocessing.MinMaxScaler()
norm_cases = min_max_scaler.fit_transform(cases)

from sklearn.decomposition import PCA

estimator = PCA (n_components = 2)
X_pca = estimator.fit_transform(norm_cases)
plt.plot(X_pca[:,0], X_pca[:,1],'x')

# Computing the similarity matrix. Here the distance function that we selected is chosen.
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean') 
matsim = dist.pairwise(norm_cases)
avSim = numpy.average(matsim)
print "%s\t%6.2f" % ('Average Distance', avSim)

# Creates the dendrogram and plots it
cut = 13     #This variable represents where the separation of the elements into clusters starts. From that point to the bottom of the plot
clusters = cluster.hierarchy.linkage(matsim, method = 'complete')
cluster.hierarchy.dendrogram(clusters, color_threshold = cut)
plt.show()

# Characterization of the data
labels = cluster.hierarchy.fcluster(clusters, cut , criterion = 'distance')
print 'Nº of clusters %d' % (len(set(labels)))     #Gives the number of clusters as it is represented
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print('Estimated number of clusters: %d' % n_clusters_)

# Calculates the mean of each of the attributes for the elements related to each cluster. Prints every mean in the attributes for every cluster
for c in range(1,n_clusters_+1):
    s = ''
    print 'Group', c
    for i in range(len(cases[0])):
        column = [row[i] for j,row in enumerate(cases) if labels[j] == c]
        if len(column) != 0:
            s = "%s,%s" % (s,numpy.mean(column))
    print s

# Representation of all the elements in the dataset into a PCA. Each color into that plot tells the cluster where the elements belong
colors = numpy.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
colors = numpy.hstack([colors] * 20)
numbers = numpy.arange(len(X_pca))
fig, ax = plt.subplots()
for i in range(len(X_pca)):
    plt.text(X_pca[i][0], X_pca[i][1], numbers[i], color=colors[labels[i]])
plt.xlim(-1, 1.5)
plt.ylim(-1, 1.5)
ax.grid(True)
fig.tight_layout()
plt.show()

# 10,24,50,101,108,112,210,239,262,300,406,407,474,490
#and 22,58,94,183,235,274,337,338,365,391,443,465,474,495,496,509:
