import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


alldata = pd.read_csv("./동해바다_파주기_통합본.csv",encoding='cp949')
themax = 0
for i in range(2,8):
    heremax = max(alldata.iloc[:,i])
    if heremax >= themax: themax = heremax

data = pd.read_csv("./eastseadata/동해/MARINE_BUOY_22105_HR_2011_2011_2018.csv", encoding='cp949')
data = data[['일시', '파주기(sec)', '유의파고(m)']]
data['일시'] = pd.to_datetime(data['일시'])


intercept = 0
for i in range(data.shape[0]):
    intercept += (themax - data['파주기(sec)'][i])/2
    plt.plot([intercept, intercept + data['파주기(sec)'][i]/4], [0, data['유의파고(m)'][i]], color='green')
    plt.plot([intercept + data['파주기(sec)'][i]/4, intercept + (3 * data['파주기(sec)'][i] / 4)], [data['유의파고(m)'][i], -1 * data['유의파고(m)'][i]], color='green')
    plt.plot([intercept + (3 * data['파주기(sec)'][i] / 4), intercept + data['파주기(sec)'][i]], [-1 * data['유의파고(m)'][i],0], color ='green')
    intercept += (themax + data['파주기(sec)'][i])/2
plt.show()
    



