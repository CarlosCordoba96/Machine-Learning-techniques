#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
from matplotlib.pylab import hist, show
import numpy
import scipy
import scipy.spatial



f = codecs.open("2009pivot.csv", "r", "utf-8")
estados = []
count = 0
for line in f:
	if count > 0: 
		# remove double quotes
		row = line.replace ('"', '').split(",")
		row.pop(0) # remove name of state
		if row != []:
			estados.append(map(float, row))
	count += 1


# http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html

sim = scipy.spatial.distance.pdist(estados , "euclidean")
avDist = numpy.average ( sim )
print ("Average Distance", avDist)

# http://matplotlib.org/api/pyplot_api.html
hist(sim)
show()

#normalized distance (between 0 and 1)

normalized = (sim-min(sim))/(max(sim)-min(sim))
avDist = numpy.average ( normalized )
print ("Normalized Average Distance", avDist)

hist(normalized)
show()
