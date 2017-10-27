# -*- coding: utf-8 -*-
"""
"""

import codecs
from numpy import corrcoef, transpose, arange
from pylab import pcolor, show, colorbar, xticks, yticks
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

# Load data 
f = codecs.open("Data\ iq_2000_2003_pivot.csv", "r", "utf-8")
states = []
count = 0
for line in f:
	if count > 0:
		# remove double quotes
		row = line.replace ('"', '').split(",")
		row.pop(0)
		if row != []:
			states.append(map(float, row))#Using float
	count += 1

# Using as much range as the number of attributes that we have, prints the Correlation Matrix
R = corrcoef(transpose(states))
pcolor(R)
colorbar()
yticks(arange(0,21),range(0,21))
xticks(arange(0,21),range(0,21))
show()

# Generates the triangle of correlation with the same elements, and prints it
sns.set(style="white")
mask = np.zeros_like(R, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(200, 10, as_cmap=True)
sns.heatmap(R, mask=mask, cmap=cmap, vmax=.8,
            square=True, xticklabels=2, yticklabels=2,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)
