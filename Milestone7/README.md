# MILESTONE 7 

The objective of this milestone is only to improve our model. In this documentation, we are gooing to explain our model in a submission-based way. This means that we are going to explain the changes in our code made for each submission. We are going to describe our score as well, and the improvement/decrease in the competition ranking.

# 2nd submission
- Rounded integer values of resulting prediction.
- Changed number of neighbour for kNN in both cities, based on the Cross Validation model of kNN script. Before that, we just applied the k value that seemed better, but after taking into account Cross Validation we saw the improvement.
- Score: 27.1202

# 3rd submission
- Removed feature 'year' in the model of both cities.
- The feature selection changed for each city. In the case of iquitos, the new features were 'weekofyear' and 'reanalysis_specific_humidity_g_per_kg'. For san juan, 'weekofyear''reanalysis_dew_point_temp_k','reanalysis_specific_humidity_g_per_kg' and 'station_max_temp_c'.
- Number of neighbours changed for both cities.
- Score: 26.0841

# 4th submission
- Removed round of the resulting 'total_cases' prediction. After checking the Mean Absolute Error and our prediction values, we finally decided that this method for rounding total cases just made the prediction more wrong than it was before.
- Score: 26.0313

# 5th submission
- Changed the way of selecting the n_neighbors value of the knn algorithm. Before we realised, we just got the minimum value on our Cross Validation, and didn't change the weights depending on the weight criteria that had lower Mean Absolute Error.
- Selected the 'distance' weights criteria of kNN for both cities.
- Score: 25.9663

# 6th submission
- We tried to apply Random Forest in our model. In order to do so, we estimated about creating 1000 decission trees for each city, with the corresponding depth for each one. San Juan random forests have depth 5, based on the study of Mean Absolute Error by the Depth of the tree that we did in Milestone 5. In the case of Iquitos, doing the same study, our trees have depth 3.
- The resulting predictions were quite different from the kNN ones. To check if the Mean Absolute Error of Random Forest prediction would be lower, we splited our Training Data in Training and Test itself. Then, we applied random forest to that training data and tried that out in the test. The results seemed very reliable, so we finally uploaded the submission.
- Score: 24.6683

# 7th submission
- We tried to merge both models, applying kNN to San Juan and Random Forest to Iquitos. That's because we thought that Random Forest didn't work in San Juan as well as in Iquitos. But we were wrong.
- Score: 25.3558
