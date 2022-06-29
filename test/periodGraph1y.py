import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("./eastseadata/동해/MARINE_BUOY_22105_HR_2021_2021_2022.csv", encoding='cp949')
data = data[['일시', '파주기(sec)', '유의파고(m)']]
data['일시'] = pd.to_datetime(data['일시'])


intercept = 0
for i in range(data.shape[0]):
    plt.plot([intercept, intercept + data['파주기(sec)'][i]/4], [0, data['유의파고(m)'][i]], color='green')
    plt.plot([intercept + data['파주기(sec)'][i]/4, intercept + (3 * data['파주기(sec)'][i] / 4)], [data['유의파고(m)'][i], -1 * data['유의파고(m)'][i]], color='green')
    plt.plot([intercept + (3 * data['파주기(sec)'][i] / 4), intercept + data['파주기(sec)'][i]], [-1 * data['유의파고(m)'][i],0], color ='green')
    intercept += data['파주기(sec)'][i]
plt.show()