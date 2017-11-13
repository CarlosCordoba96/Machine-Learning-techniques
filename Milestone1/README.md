# Milestone 1:

The goal of this Milestone is to filter the data that has been given to us, to retrieve only the data from the 2000-2003 period in Iquitos; and compute the correlation coefficient and pca test to study the dataset.

## 1. Filtering the data

Besides retrieving only the data for Iquitos in 2000-2003 from the original dataset, the columns 'year', 'city', 'date' have been removed as they are not necessary for future computations. Also, not valid values have been convertet into type NaN to ease future steps. These task are done in the file [01_pivot.py](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Activity1/01_pivot.py)

## 2. Correlation Coefficient

The correlation coefficient helps us to see the simetry of our dataset. We have computed the correlation coefficient and represented it in two different graphs. This task is done in the file [02_correlation.py](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Activity1/02_correlation.py)

![first graph](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone1/Images/correlation_1.png)

![second graph](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone1/Images/correlation_2.png). 


## 3. PCA

The PCA is a test used to check the internal structure of the data. This is computed in the file [03_pca.py](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Activity1/03_pca.py) . The resulting graph is shown in the picture below:

![PCA](https://github.com/CarlosCordoba96/Machine-Learning-techniques/blob/master/Milestone1/Images/pca.png)

## Final thoughts

After seeing the different graphs we can say that our data is not very symetric; as there are some zones were the data is correlated but, on the other hand there are other zones where is very visible that the data is more diverse.
