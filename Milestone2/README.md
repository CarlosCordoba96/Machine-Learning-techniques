# Milestone 2

1. Study of the different distances and election of one for the characterization.
 
We have tried different distances on our file, and after a few tries decided to chose the Euclidean distance and combine it with a 'Complete' cluster hierarchy for the Denogram process. Our criterion was distance. This can be seen in the file [cluster_hierarchical.py](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone2/cluster_hierarchical.py)

We studied the results in hierarchical clustering and PCA. In the second one, we could see the dimensional representation of all the elements divided in the clusters. We could see some elements that could act as outliers in PCA but appeared in a grouped cluster in the hierarchical representation, while some elements in PCA that seems to be grouped in a cluster are represented as outliers in clustering.

With the array 'labels' generated, we have every element of our data set related to the cluster where it belongs. That could help us in a lot of ways, from checking it to get quick information to add it into our data set and filter our elements, work with them depending on their cluster.

2. Labeling and description of the clusters.

We have found 9 clusters in total. Using the 'labels' information as a new feature in our data, we filtered this information in order to study the the information of the elements corresponding to each cluster/group of cluster that will be defined (in alphabetical order). Some groups that have several clusters inside them, those clusters are grouped because they have elements that are very related (in some features), even when they are different in representation.

A: A, B y C
B: B y C
C: B y C
D: D, E y F
E: E y F
F: E y F
G: G, H e I
H: I y H
I: I y H

3. The best dendogram
