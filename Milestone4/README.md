# Milestone 4 - Decision Tree for regression

## 1.- Studying the correlation between features and total cases

After this step, we have obtained this correlation graph:

![correlation graph](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone4/img/correlation.png).

We have studied the correlation of our dataset variables related to dengue cases. From this information, we have concluded that variables such as:

* reanalysis_dew_point_temp_k : Mean dew point temperature
* reanalysis_min_air_temp_k : Minimum air temperature
* reanalysis_relative_humidity_percent : Mean relative humidity
* reanalysis_specific_humidity_g_per_kg : Mean specific humidity
* station_min_temp_c : Minimum temperature

They heavily influentiate the dengue cases. This leads us to think that the temperature and the humidity of a certain zone matters to dengue cases of our dataset.

## 2.- Feature Selection

Based on the previous conclusion, we have removed all features except the ones previously mentioned, 'weekofyear' and 'year' and stored the selected features in the variable "selected_features".

## 3.-  Building a Decision Tree Model 
* Max depth: Studying our algorithm, we concluded that our system is in a normal size, not overfitted or underfitted. The best depth to create our decision tree, taking into account this graph, would be 11, where the error is minimum as our study guess.

![mae](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone4/img/mae.png).

* Features Relevances: To select what features of our dataset should be included into the decision tree, we decided to apply a study on those attributes, in order to know the relevance that we have in our dengue cases.

![feature_relevances](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone4/img/feature_relevances.PNG).

With this results we realised that some of the more correlated features don't have any information to the relevance of the cases. With this graph, we decided to only apply two features in our decision tree: 'reanalysis_dew_point_temp_k' and 'station_min_temp_c'.

* Tree Model: That is our tree model, created in the file 'tree.dot'. It has depth 3 and the decisions are based on our selected features. First, on the 'reanalysis_dew_point_temp_k', and using 'station_min_temp_c' in the two different resulting sibblings of depth 1.

![decision_tree](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone4/img/decission_tree.png).

Based on the number of samples that each leaf, we could think that the most-right leaf could represent a group of outliers, due to the fact that they have the smallest number of elements in the decision tree (11).

* Cross Validation: This is the cross validation diagram resulting from our regression decision (taking 'reanalysis_dew_point_temp_k' and 'station_min_temp_c' as features to create the tree model). What we can say about our cv is that our model is in general of a normal size. Althought there are some cases where the data is overfitted or underfitted, the model gets a good mean of variance for many depths.

![cross_validation](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone4/img/cross_validation.png).
