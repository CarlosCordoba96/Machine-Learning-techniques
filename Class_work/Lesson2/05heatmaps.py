#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import matplotlib.pyplot as plt
import sklearn.neighbors
# http://scikit-learn.org/stable/modules/preprocessing.html
from sklearn import preprocessing 

def display_heatmap(matsim): 
	fig, ax = plt.subplots()

	# http://matplotlib.org/api/pyplot_api.html

	ax.imshow(matsim, cmap=plt.cm.hot, interpolation='nearest')
	ax.set_title('similarity matrix')

	# Move left and bottom spines outward by 10 points
	ax.spines['left'].set_position(('outward', 21))
	ax.spines['bottom'].set_position(('outward', 21))
	# Hide the right and top spines
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	# Only show ticks on the left and bottom spines
	ax.yaxis.set_ticks_position('left')
	ax.xaxis.set_ticks_position('bottom')

	plt.show()

# another option to plot a heat map https://plot.ly/python/heatmaps/


f = codecs.open("2009pivot.csv", "r", "utf-8")
states = []
count = 0
for line in f:
	if count > 0: 
		# remove double quotes
		row = line.replace ('"', '').split(",")
		row.pop(0)
		if row != []:
			states.append(map(float, row))
	count += 1


# http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.DistanceMetric.html
# 3 normalizaciones disstintas: preprocessing.scale(estandariza), min-max scaler (pasar
# todo a 0/1), normalized lo reduce a información unitaria
states_scaled = preprocessing.scale(states) # zero mean and unit variance.
min_max_scaler = preprocessing.MinMaxScaler()
states_minmax = min_max_scaler.fit_transform(states) #  scaling features to lie between a given minimum and maximum value, often between zero and one.
states_normalized = preprocessing.normalize(states) 
print states_normalized

dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
matsim_scaled = dist.pairwise(states_scaled)
matsim_minmax = dist.pairwise(states_minmax)
matsim_norm = dist.pairwise(states_normalized)


#print matsim_minmax

display_heatmap(matsim_scaled) # same as last
display_heatmap(matsim_minmax) #
display_heatmap(matsim_norm) # f scaling individual samples to have unit norm. 
