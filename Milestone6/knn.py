import pandas as pd

def loaddata():
    #read sanjuan
    sj = pd.read_csv('Data/sanjuan/dengue_features_train.csv')
    sj2=pd.read_csv('Data/sanjuan/dengue_labels_train.csv')
    sanjuan = pd.merge(sj, sj2, on=['city', 'year','weekofyear'])
    
    sanjuan=sanjuan.drop(sanjuan.index[[88,140,400,452,752,712,764,495]])#principal outliers
    
    sanjuan=sanjuan.drop(sanjuan.index[[700,502,361,253,254,330,493]])
    sanjuan = sanjuan.fillna(sanjuan.mean())#There is some data as NaN
    
    
    #read iquitos
    iq = pd.read_csv('Data/iquitos/dengue_features_train.csv')
    iq2=pd.read_csv('Data/iquitos/dengue_labels_train.csv')
    iquitos = pd.merge(iq, iq2, on=['city', 'year','weekofyear'])
    iquitos=iquitos.drop(iquitos.index[[22,58,94,183,235,274,337,338,365,391,443,465,474,495,496,509]])
    iquitos=iquitos.drop(iquitos.index[[101,3,50,300,10,112,268,239,474]])
    iquitos = iquitos.fillna(iquitos.mean())#There is some data as NaN
    frames=[sanjuan,iquitos]
    data=pd.concat(frames)
    return data


data=loaddata()
print data