import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

#Loading data
def loaddata():
    #read sanjuan
    sj = pd.read_csv('Data/sanjuan/dengue_features_train.csv')
    sj2=pd.read_csv('Data/sanjuan/dengue_labels_train.csv')
    sanjuan = pd.merge(sj, sj2, on=['city', 'year','weekofyear'])
    
    sanjuan=sanjuan.drop(sanjuan.index[[88,140,400,452,752,712,764,495]])#principal outliers
    
    sanjuan=sanjuan.drop(sanjuan.index[[700,502,361,253,254,330,493]])
    sanjuan = sanjuan.fillna(sanjuan.mean())#There is some data as NaN
    
    return sanjuan


data=loaddata()

#Parametrization
X = data[['weekofyear','year','reanalysis_specific_humidity_g_per_kg']]
y = data['total_cases']
xx = np.stack (i for i in range (len(y)))


#Cross validation analysis
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

min_val=1000000
j=0
for i in range(0,len(total_scores)):
    if total_scores[i]<min_val:
        min_val=total_scores[i]
        j=i
        
print "the min value is:"
    
print "{} - with value- {}".format(j,min_val)

# Fit regression model
n_neighbors = 28

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
datosTest = pd.read_csv("Data/dengue_features_test_sanjuan.csv")
datosTest=datosTest.fillna(datosTest.mean())
test = datosTest[['weekofyear','year','reanalysis_specific_humidity_g_per_kg']]


# prediction
knn = neighbors.KNeighborsRegressor(n_neighbors, weights='distance')
prediccion = knn.fit(X,y).predict(test)


# show prediction

xx = np.stack(i for i in range(len(prediccion)))
plt.subplot(2, 1, i + 1)
plt.plot(xx, prediccion, c='g', label='prediction')
plt.axis('tight')
plt.legend()
plt.title("KNeighborsRegressor (k = %i, weights = '%s')" % (n_neighbors,weights))

plt.show()
for i in range(0,len(prediccion)):
    prediccion[i]=round(prediccion[i],0)
    
datosTest['total_cases']=prediccion

datosTest['total_cases']=datosTest['total_cases'].astype(int)

final=datosTest[['city','year','weekofyear','total_cases']]


final.to_csv('predictedsanjuan.csv',index=False)



