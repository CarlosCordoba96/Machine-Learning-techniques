#!/usr/bin/env python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy


#http://docs.scipy.org/doc/scipy/reference/cluster.html
from scipy import cluster
from sklearn import preprocessing 
import sklearn.neighbors

# 0. Load Data
import loaddata
states,names = loaddata.load_data_usa("2009pivot.csv")
 
 
#1. Normalization of the data
#http://scikit-learn.org/stable/modules/preprocessing.html
from sklearn import preprocessing 
min_max_scaler = preprocessing.MinMaxScaler()
states = min_max_scaler.fit_transform(states)
	
# 2. Compute the similarity matrix
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean') #'single' da el grupo más compacto y los outliers a los lados
matsim = dist.pairwise(states)
avSim = numpy.average(matsim)
print "%s\t%6.2f" % ('Average Distance', avSim)

# 3. Building the Dendrogram	
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage
clusters = cluster.hierarchy.linkage(matsim, method = 'complete')
# http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.cluster.hierarchy.dendrogram.html
cluster.hierarchy.dendrogram(clusters, color_threshold = 4)
plt.show()


# 4. Cutting the dendrogram
#Forms flat clusters from the hierarchical clustering defined by the linkage matrix clusters
# introduce the value after dendrogram visualization

# cut = float(input("Threshold cut:"))
clusters = cluster.hierarchy.fcluster(clusters, 4 , criterion = 'distance')

# 5. Show the usa Map
import mapausa
mapausa.show_usa_map(clusters)

