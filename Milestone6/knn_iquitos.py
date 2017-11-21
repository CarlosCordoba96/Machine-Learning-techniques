import pandas as pd

def loaddata():
    #read sanjuan
#    sj = pd.read_csv('Data/sanjuan/dengue_features_train.csv')
#    sj2=pd.read_csv('Data/sanjuan/dengue_labels_train.csv')
#    sanjuan = pd.merge(sj, sj2, on=['city', 'year','weekofyear'])
#    
#    sanjuan=sanjuan.drop(sanjuan.index[[88,140,400,452,752,712,764,495]])#principal outliers
#    
#    sanjuan=sanjuan.drop(sanjuan.index[[700,502,361,253,254,330,493]])
#    sanjuan = sanjuan.fillna(sanjuan.mean())#There is some data as NaN
    
    
    #read iquitos
    iq = pd.read_csv('Data/iquitos/dengue_features_train.csv')
    iq2=pd.read_csv('Data/iquitos/dengue_labels_train.csv')
    iquitos = pd.merge(iq, iq2, on=['city', 'year','weekofyear'])
    iquitos=iquitos.drop(iquitos.index[[22,58,94,183,235,274,337,338,365,391,443,465,474,495,496,509]])
    iquitos=iquitos.drop(iquitos.index[[101,3,50,300,10,112,268,239,474]])
    iquitos = iquitos.fillna(iquitos.mean())#There is some data as NaN
#    frames=[sanjuan,iquitos]
#    data=pd.concat(frames)
    return iquitos


data=loaddata()
#print data

# #############################################################################
# Generate sample data
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

#np.random.seed(0)
X = data[['weekofyear','year','reanalysis_min_air_temp_k']]
#T = np.linspace(0, 5, 500)[:, np.newaxis]
y = data['total_cases']
xx = np.stack (i for i in range (len(y)))
# Add noise to targets
#y[::5] += 1 * (0.5 - np.random.rand(8))


# 1. CROSS VALIDATION ANALYSIS
from sklearn import neighbors
from sklearn.cross_validation import cross_val_score

for i, weights in enumerate(['uniform', 'distance']):
    total_scores = []
    for n_neighbors in range(1,30):
        knn = neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
        knn.fit(X,y)
        scores = -cross_val_score(knn, X,y, 
                                    scoring='neg_mean_absolute_error', cv=10)
        total_scores.append(scores.mean())
    
    plt.plot(range(0,len(total_scores)), total_scores, 
             marker='o', label=weights)
    plt.ylabel('cv score')

plt.legend()
plt.show() 


# #############################################################################
# Fit regression model
n_neighbors = 9

for i, weights in enumerate(['uniform', 'distance']):
    knn = neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
    y_prediction = knn.fit(X, y).predict(X)

    plt.subplot(2, 1, i + 1)
    plt.plot(xx, y , c= 'k', label = 'data')
    plt.plot(xx, y_prediction, c='g', label='prediction')
    plt.axis('tight')
    plt.legend()
    plt.title("KNeighborsRegressor (k = %i, weights = '%s')" % (n_neighbors,
                                                                weights))

plt.show()

# 