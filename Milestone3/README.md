
# 1. Data Set

Studying the clustering in Milestone 2, we took a look at two clusters (2 and 3) which are made of many individual elements. We defined them as 'outliers', so we decided to remove those outliers to get a better performance of k-means algorithm.
The elements that were removed belonged to clusters 2 and 3: Cluster 2 {10, 20, 25, 115} & Cluster 3 {51, 111, 104, 159}. We removed all of them and not some specific well-known outliers because if they belong to the same cluster, even some elements that don't look as outliers were more related to the outliers than the rest of elements. Based on that thought, we made that decision.

# 2. K-Means

At the ending of Milestone 2, we decided to group our 8 clusters in 3 different groups, where the elements where related in attributes or as individuals. To keep that relation between the elements, we set up our value of k at 3, in order to try to represent the same elements in the same groups. COMPROBAR CON LABELS().
The k-means method that we dediced to use is 'k-means++'. We tried out both methods, k-means++ and random, but the representation using random felt more ambiguous. However, the other representation seemed clearer and easier to understand and study.

# 3. Results

![K-Means++](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone3/k-means%2B%2B.png)

Here we have the graphical representation of our application of k-means. We got 3 separated groups, which we can study and compare to hierarchical agglomerative clustering algorithm.
-The purple centroid groups most of the elements that belonged to cluster 4, so we can say that those elements are very related in both algorithms.
-The green centroid represents a large variety of elements, represented in different clusters. We can't say much about this aggrupation or the concrete attributes of any of them.
-The yellow centroid has the rest of the principal clusters in Milestone 2, being a well separated group but that doesn't give us much information, less than the hierarchical agglomerative clustering algorithm could give us.
