import pandas as pd
iq = pd.read_csv('predictediquitos.csv')
sj = pd.read_csv('predictedsanjuan.csv')
result= sj.append(iq)
result.to_csv('predicted.csv',index=False)