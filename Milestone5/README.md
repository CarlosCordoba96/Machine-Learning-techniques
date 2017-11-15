# Milestone 5

The objective of this milestone was to take all the knowledge we obtained from previous milestones and apply it to new datasets, in order to do the feature selection of a model for each new dataset. The new datasets are iquitos and san juan cities, separated in two different datasets to generate two different models.

## Iquitos
* Clustering. With clustering, we got 5 different groups. After studying the PCA representation of the clusters, we decided to remove some outliers that could affect negatively to our model.
![clustering](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone5/iquitos/images/pca.png).
* Feature Selection. Cross validation told us to apply a depth of 3 in our model. Looking for the features selection we got the following result:

![features](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone5/iquitos/images/feature_relevancies.png).

'weekofyear' and 'year' are the most relevant features for creating a model. So those are the ones that would be introduced in our decision tree.

## San Juan
* Clustering. With clustering, we got 6 different groups. After studying the PCA representation of the clusters, we decided to remove some outliers that could affect negatively to our model.
![clustering](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone5/san%20juan/Img/clustering.png).
* Feature Selection. Cross validation results were positive about creating our model with a depth of 5. Appyling that depth to our regressor decision tree model, this is the features selection result that we got.

![features](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone5/san%20juan/Img/Features%20relevances.PNG).

'year' and 'weekofyear' are the most relevant features to define our model in the decision tree.
