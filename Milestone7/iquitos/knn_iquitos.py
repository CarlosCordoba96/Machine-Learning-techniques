import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

#Loading data
def loaddata():   

    #read iquitos
    iq = pd.read_csv('Data/dengue_features_train.csv')
    iq2=pd.read_csv('Data/dengue_labels_train.csv')
    iquitos = pd.merge(iq, iq2, on=['city', 'year','weekofyear'])
    iquitos=iquitos.drop(iquitos.index[[22,58,94,183,235,274,337,338,365,391,443,465,474,495,496,509]])
    iquitos=iquitos.drop(iquitos.index[[101,3,50,300,10,112,268,239,474]])
    iquitos = iquitos.fillna(iquitos.mean())#There is some data as NaN

    return iquitos

data=loaddata()

feat=['weekofyear','reanalysis_specific_humidity_g_per_kg']

#Parametrization
X = data[feat]
y = data['total_cases']
xx = np.stack (i for i in range (len(y)))


#Cross validation analysis
from sklearn.cross_validation import cross_val_score
min_val=1000000
j=0
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
    for z in range(0,len(total_scores)):
        if total_scores[z]<min_val:
            min_val=total_scores[z]
            j=z
plt.legend()
plt.show()
       
print "the min value is:"
    
print "{} - with value- {}".format(j,min_val)

import numpy
# Fit regression model
n_neighbors = 6

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

#read test data
datosTest = pd.read_csv("Data/dengue_features_test_iquitos.csv")
datosTest=datosTest.fillna(datosTest.mean())
test = datosTest[feat]


# prediction
knn = neighbors.KNeighborsRegressor(n_neighbors, weights='distance')
prediccion = knn.fit(X,y).predict(test)


# show prediction

xx = np.stack(i for i in range(len(prediccion)))
plt.subplot(2, 1, i + 1)
plt.plot(xx, prediccion, c='g', label='prediction')
plt.axis('tight')
plt.legend()
weights='uniform'
plt.title("KNeighborsRegressor (k = %i, weights = '%s')" % (n_neighbors ,weights))

plt.show()

#for i in range(0,len(prediccion)):
#    prediccion[i]=round(prediccion[i],0)

datosTest['total_cases']=prediccion

datosTest['total_cases']=datosTest['total_cases'].astype(int)

final=datosTest[['city','year','weekofyear','total_cases']]


final.to_csv('predictediquitos.csv',index=False)