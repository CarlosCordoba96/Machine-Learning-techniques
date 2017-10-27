# Milestone 2

# Study and selection of the different distances for the characterization.
 
We have tried different distances on our script [cluster_hierarchical.py](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone2/cluster_hierarchical.py), and after a few tries decided to chose the Euclidean distance and combine it with a 'Complete' cluster hierarchy for the Denogram process. Our criterion was distance. 

We studied the results in hierarchical clustering and PCA. In the second one, we could see the dimensional representation of all the elements divided in the clusters. There were some elements that could act as outliers in PCA but appeared in a grouped cluster in the hierarchical representation, while some elements in PCA that seemed to be grouped in a cluster are represented as outliers in clustering. Here you can see the results:

![Clustering](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone2/Images/Clustering.jpg)
![PCA](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone2/Images/PCA_Cluster.jpg)

Once the array 'labels' is generated, we have every element of our data set related to the cluster where it belongs. This can help us in many ways, like checking it to get quick information to add to our data set and help filtering our elements; and work with them depending on their cluster.

# Labeling and descripting clusters.

We have found 8 clusters in total. Using the 'labels' information as a new feature in our data, we filtered this information in order to study the information of the elements corresponding to each cluster/group of cluster that will be defined (in alphabetical order). 

Some groups have several clusters inside them, which are grouped because they have elements that are very related in some features, even when they are different in representation. After analyzing the data we have conclude that there are 3 main clusters:

**Cluster A**: This cluster is formed by groups 1,2 and 3. It is characterized for having far more outliers than any of the other groups. This is probably the data about precipitation, as it has very different values.

**Cluster B**: This cluster is formed of groups 4 and 5. This cluster is formed due to similarities in the means of features such as ndvi_ne,	ndvi_nw,	ndvi_se, or	ndvi_sw.
 

**Cluster C**: This cluster is formed of groups 6,7 and 8. This is the bigger cluster found. It has very similar features, but you can appreciate some big distances among of them. This fact leads us to think that it contains features on the temperature.


