# -*- coding: utf-8 -*-
"""
Created on Wed Oct 04 16:56:48 2017

@author: Alvaro
"""

import matplotlib.pyplot as plt
import numpy


#http://docs.scipy.org/doc/scipy/reference/cluster.html
from scipy import cluster
from sklearn import preprocessing 
import sklearn.neighbors

# 0. Load Data
import loaddata
cases = loaddata.load_data_usa("Data/iq_2000_2003_pivot.csv")
 
 
### 2. Normalization of the data
min_max_scaler = preprocessing.MinMaxScaler()
norm_cases = min_max_scaler.fit_transform(cases)

### 3. Compute the similarity matrix
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean') 
matsim = dist.pairwise(norm_cases)
avSim = numpy.average(matsim)
print "%s\t%6.2f" % ('Average Distance', avSim)

### 4. Building the Dendrogram	
cut = 5
clusters = cluster.hierarchy.linkage(matsim, method = 'complete')
cluster.hierarchy.dendrogram(clusters, color_threshold = cut)
plt.show()

### 5. Characterization
labels = cluster.hierarchy.fcluster(clusters, cut , criterion = 'distance')
print 'Nº of clusters %d' % (len(set(labels)))

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print('Estimated number of clusters: %d' % n_clusters_)
     

for c in range(1,n_clusters_+1):
    s = ''
    print 'Group', c
    for i in range(len(cases[0])):
        column = [row[i] for j,row in enumerate(cases) if labels[j] == c]
        if len(column) != 0:
            s = "%s,%s" % (s,numpy.mean(column))
    print s

# Sacar numero de elementos de cada cluster