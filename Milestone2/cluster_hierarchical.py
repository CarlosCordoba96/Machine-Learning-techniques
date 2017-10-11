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

#0.5. Tools for PCA
from sklearn.decomposition import PCA
estimator = PCA (n_components = 2)
X_pca = estimator.fit_transform(norm_cases)

plt.plot(X_pca[:,0], X_pca[:,1],'x')

### 3. Compute the similarity matrix
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean') 
matsim = dist.pairwise(norm_cases)
avSim = numpy.average(matsim)
print "%s\t%6.2f" % ('Average Distance', avSim)

### 4. Building the Dendrogram	
cut = 7
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

# PCA de clúster
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