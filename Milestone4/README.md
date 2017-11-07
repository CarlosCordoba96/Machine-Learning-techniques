# Milestone 4 - Decission Tree for regression

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
* Max depth

![mae](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone4/img/mae.png).

* Features Relevances

![feature_relevances](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone4/img/feature_relevances.PNG).
* Tree Model

![decision_tree](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone4/img/decission_tree.png).
* Cross Validation

![cross_validation](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone4/img/cross_validation.png).
