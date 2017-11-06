# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 19:30:57 2017

@author: Julian
"""
#imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import graphviz
# 0.1 load data
information = pd.read_csv('Data/dengue_features_train.csv')
information2=pd.read_csv('Data/dengue_labels_train.csv')
result = pd.merge(information, information2, on=['city', 'year','weekofyear'])

result = result.fillna(0)#There is some data as NaN

#0.2 Explore Data
plt.rcdefaults()

#0.2.1 Univariate Histograms
# 
result.hist()
plt.show()
#0.2.2 Density Plots
result.plot(kind='density', subplots=True, layout=(6,4), sharex=False)
plt.show()
##0.2.3 Scatterplot matrix
##from pandas.tools.plotting import scatter_matrix
##scatter_matrix(result)
##plt.show()

#0.2.4

# NOTE: Low correlation means there's no linear relationship; 
# it doesn't mean there's no information in the feature that predicts the target.


from scipy.stats.stats import pearsonr 
corr = [pearsonr(result['ndvi_ne'], result['total_cases'])[0],
        pearsonr(result['ndvi_nw'], result['total_cases'])[0],
        pearsonr(result['ndvi_se'], result['total_cases'])[0],
        pearsonr(result['ndvi_sw'], result['total_cases'])[0],
        pearsonr(result['precipitation_amt_mm'], result['total_cases'])[0],
        pearsonr(result['reanalysis_air_temp_k'], result['total_cases'])[0],
        pearsonr(result['reanalysis_avg_temp_k'], result['total_cases'])[0],
        pearsonr(result['reanalysis_dew_point_temp_k'], result['total_cases'])[0],
        pearsonr(result['reanalysis_max_air_temp_k'], result['total_cases'])[0],
        pearsonr(result['reanalysis_min_air_temp_k'], result['total_cases'])[0],
        pearsonr(result['reanalysis_precip_amt_kg_per_m2'], result['total_cases'])[0],
        pearsonr(result['reanalysis_relative_humidity_percent'], result['total_cases'])[0],
        pearsonr(result['reanalysis_sat_precip_amt_mm'], result['total_cases'])[0],
        pearsonr(result['reanalysis_specific_humidity_g_per_kg'], result['total_cases'])[0],
        pearsonr(result['reanalysis_tdtr_k'], result['total_cases'])[0],
        pearsonr(result['station_avg_temp_c'], result['total_cases'])[0],
        pearsonr(result['station_diur_temp_rng_c'], result['total_cases'])[0],
        pearsonr(result['station_max_temp_c'], result['total_cases'])[0],
        pearsonr(result['station_min_temp_c'], result['total_cases'])[0],
        pearsonr(result['station_precip_mm'], result['total_cases'])[0]]

 
features= ('ndvi_ne','ndvi_nw','ndvi_se','ndvi_sw','precipitation_amt_mm','reanalysis_air_temp_k','reanalysis_avg_temp_k','reanalysis_dew_point_temp_k','reanalysis_max_air_temp_k','reanalysis_min_air_temp_k','reanalysis_precip_amt_kg_per_m2','reanalysis_relative_humidity_percent','reanalysis_sat_precip_amt_mm','reanalysis_specific_humidity_g_per_kg','reanalysis_tdtr_k','station_avg_temp_c','station_diur_temp_rng_c','station_max_temp_c','station_min_temp_c','station_precip_mm')
my_features=('reanalys_dew_point_temp_k','reanalysis_min_temp_c')
y_pos = np.arange(len(corr))
 
plt.bar(y_pos, corr, align='center', alpha=0.5)
plt.xticks(y_pos, features,rotation='vertical')
plt.ylabel('Correlation')
plt.title('Correlation features vs target')

plt.show()
#Feature selection by removing not wanted features
features_selected = result.drop(result.columns[[0,1,2,3,4,5,6,7,8,9,10,12,14,16,18,19,20,21,23]], axis=1)

###################
features_selected2 = result.drop(result.columns[[0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,23]], axis=1)
##################

#1. Build the model
from sklearn.tree import DecisionTreeRegressor

#1.1 Model Parametrization 
# criterion: mse mean squared error, which is equal to variance reduction as feature selection criterion
#splitter: best/random
# max_depth: low value avoid overfitting
regressor = DecisionTreeRegressor(criterion='mse', max_depth=2, random_state=0)
#1.2 Model construction
#regressor.fit(bikes[['temperature', 'humidity', 'windspeed']], bikes['count'])
# one feature predictor
regressor.fit(features_selected[['reanalysis_dew_point_temp_k','reanalysis_min_air_temp_k','reanalysis_relative_humidity_percent','reanalysis_specific_humidity_g_per_kg','station_min_temp_c']], features_selected['total_cases'])

####
regressor2 = DecisionTreeRegressor(criterion='mse', max_depth=2, random_state=0)
regressor2.fit(features_selected2[['reanalysis_dew_point_temp_k','station_min_temp_c']], features_selected['total_cases'])
####

# 2.2 Feature Relevances

print 'Feature Relevancies'
list1 = zip(features_selected, regressor.feature_importances_)
from tabulate import tabulate
print tabulate(list1, headers=['Feature', 'Relevance'])

#2.  Model Visualization 
 
# Don't forget pip install graphviz
from sklearn.tree import export_graphviz
dot_data = export_graphviz(regressor2, out_file='tree.dot', feature_names=my_features, 
                           filled=True, rounded=True)
graph = graphviz.Source(dot_data)  
graph 

# 2.2 Model Plot

# This visualization is only useful for a model of two predictors

nx = 30
ny = 30
# creating a grid of points
x_reanalysis_dew_point_temp_k = np.linspace(-5, 40, nx)
y_station_min_temp_c = np.linspace(20, 80, ny)
xx, yy = np.meshgrid(x_reanalysis_dew_point_temp_k, y_station_min_temp_c)
# evaluating the regresson on all the points
z_total_cases = regressor2.predict(np.array([xx.flatten(), yy.flatten()]).T)
zz = np.reshape(z_total_cases, (nx, ny))


fig = plt.figure(figsize=(8, 8))
# plotting the predictions
plt.pcolormesh(x_reanalysis_dew_point_temp_k, y_station_min_temp_c, zz, cmap=plt.cm.YlOrRd)
plt.colorbar(label='Cases predicted') # add a colorbar on the right
# plotting also the observations
plt.scatter(features_selected2['reanalysis_dew_point_temp_k'], features_selected2['station_min_temp_c'], s=features_selected['total_cases']/25.0, c='g')
# setting the limit for each axis
plt.xlim(np.min(x_reanalysis_dew_point_temp_k), np.max(x_reanalysis_dew_point_temp_k))
plt.ylim(np.min(y_station_min_temp_c), np.max(y_station_min_temp_c))
plt.xlabel('reanalysis_dew_point_temp_k')
plt.ylabel('station_min_temp_c')
plt.show()

# Compute the max 
mae = []
from sklearn.metrics import mean_absolute_error
for i in range(2, 30):
    regressor2 = DecisionTreeRegressor(max_depth=i)
    regressor2.fit(features_selected2[['reanalysis_dew_point_temp_k', 'station_min_temp_c']], features_selected2['total_cases'])
    pred_values = regressor2.predict(features_selected2[['reanalysis_dew_point_temp_k', 'station_min_temp_c']])
    maev = mean_absolute_error(features_selected2['total_cases'],pred_values)
    mae.append(maev)
    
# Plot mae   
plt.plot(range(2,30), mae, marker='o')
plt.xlabel('max_depth')
plt.ylabel('mae')
plt.show()


# CROSS VALIDATION ANALYSIS
from sklearn.cross_validation import cross_val_score

total_scores = []
from sklearn.metrics import mean_absolute_error
for i in range(2, 30):
    regressor2 = DecisionTreeRegressor(max_depth=i)
    regressor2.fit(features_selected2[['reanalysis_dew_point_temp_k', 'station_min_temp_c']], features_selected2['total_cases'])
    scores = -cross_val_score(regressor2, features_selected2[['reanalysis_dew_point_temp_k', 'station_min_temp_c']],
            features_selected2['total_cases'], scoring='neg_mean_absolute_error', cv=10)
    total_scores.append(scores.mean())

plt.plot(range(2,30), total_scores, marker='o')
plt.xlabel('max_depth')
plt.ylabel('cv score')
plt.show()  