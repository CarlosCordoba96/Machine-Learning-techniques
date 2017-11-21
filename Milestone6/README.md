# MILESTONE 6 

The objective of this Milestone is to apply all the previous knowledge on our featured dataset to generate a feature selection for each city. Some parametrization tests as well as the kNN are also computed in order to produce the final results.

## Feature Selection
Finally, we decided to include some new features in our model, respect to the previous milestone. In the 'iquitos' prediction, we added 'reanalysis_min_air_temp_k' to 'weekofyear' and 'year', while selecting on 'san juan', we added '' to our model.

## Parametrization
In both parametrizations of our model we selected as 'X' axis our selected features, and 'total_cases' for 'y' axis.

## Model generation
We applied a cross validation analysis for each of the datasets, in order to know our k (number of neighbours). In case of 'iquitos', the number of neighbours is 9. For 'san juan' it is 8

Iquitos

![cv_iq](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone6/img/iq/crossvalidation_iq.png)

San Juan

![cv_sj](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone6/img/sj/crossvalidation_sj.png)

The application of our model into the training data itself is the following.

Iquitos

![knn_iq](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone6/img/iq/knn1_iq.png)

San Juan

![knn_sj](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone6/img/sj/knn1_sj.png)

## Final Results
With both prediction model that we got for each city, we applied them to the dataset that belongs to the test phase. Applying our model, these are the results that we obtained for the total_cases attribute.

Iquitos

![pred_iq](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone6/img/iq/prediction_iq.png)

San Juan

![pred_sj](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone6/img/sj/prediction_sj.png)

We submitted our prediction recently, and this is the result that we got: '27.6106'. We're looking for decrease that score in the next deliverable.
![score](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone6/img/Competition.PNG)
