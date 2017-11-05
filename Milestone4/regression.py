# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 19:30:57 2017

@author: Julian
"""
#imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# 0.1 load data
information = pd.read_csv('Data/dengue_features_train.csv')
information2=pd.read_csv('Data/dengue_labels_train.csv')
result = pd.merge(information, information2, on=['city', 'year','weekofyear'])


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
corr = [pearsonr(result['ndvi_ne'], result['total_cases'])[0], pearsonr(result['ndvi_se'], result['total_cases'])[0],
        pearsonr(result['ndvi_sw'], result['total_cases'])[0], pearsonr(result['precipitation_amt_mm'], result['total_cases'])[0],
        pearsonr(result['reanalysis_air_temp_k'], result['total_cases'])[0], pearsonr(result['reanalysis_avg_temp_k'], result['total_cases'])[0],
        pearsonr(result['reanalysis_dew_point_temp_k'], result['total_cases'])[0], pearsonr(result['reanalysis_max_air_temp_k'], result['total_cases'])[0],
        pearsonr(result['reanalysis_min_air_temp_k'], result['total_cases'])[0], pearsonr(result['reanalysis_precip_amt_kg_per_m2'], result['total_cases'])[0],
        pearsonr(result['reanalysis_relative_humidity_percent'], result['total_cases'])[0], pearsonr(result['reanalysis_sat_precip_amt_mm'], result['total_cases'])[0],
        pearsonr(result['reanalysis_specific_humidity_g_per_kg'], result['total_cases'])[0], pearsonr(result['reanalysis_tdtr_k'], result['total_cases'])[0],
        pearsonr(result['station_avg_temp_c'], result['total_cases'])[0], pearsonr(result['station_diur_temp_rng_c'], result['total_cases'])[0],
        pearsonr(result['station_max_temp_c'], result['total_cases'])[0], pearsonr(result['station_min_temp_c'], result['total_cases'])[0],
        pearsonr(result['station_precip_mm'], result['total_cases'])[0]]

 
features= ('ndvi_ne','ndvi_nw','ndvi_se','ndvi_sw','precipitation_amt_mm','reanalysis_air_temp_k','reanalysis_avg_temp_k','reanalysis_dew_point_temp_k','reanalysis_max_air_temp_k','reanalysis_min_air_temp_k','reanalysis_precip_amt_kg_per_m2','reanalysis_relative_humidity_percent','reanalysis_sat_precip_amt_mm','reanalysis_specific_humidity_g_per_kg','reanalysis_tdtr_k','station_avg_temp_c','station_diur_temp_rng_c','station_max_temp_c','station_min_temp_c','station_precip_mm')
y_pos = np.arange(len(features))
 
plt.bar(y_pos, corr, align='center', alpha=0.5)
plt.xticks(y_pos, features)
plt.ylabel('Correlation')
plt.title('Correlation features vs target')

plt.show()
