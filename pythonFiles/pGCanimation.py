from numpy import block
import pandas as pd
import matplotlib.pyplot as plt
import time

alldata = pd.read_csv("./동해바다_파주기_통합본.csv",encoding='cp949')
alldata_height = pd.read_csv("./동해바다_유의파고_통합본.csv" ,encoding='cp949')
# 전체 데이터 중 주기의 최댓값 찾기
themax = 0
for i in range(2,8):
    heremax = max(alldata.iloc[:,i])
    if heremax >= themax: themax = heremax


# heightmax = 0
# for i in range(2,8):
#     heremax = max(alldata_height.iloc[:,i])
#     if heremax >= heightmax: heightmax = heremax

# 파주기, 유의파고가 있는 통합본 불러오기, fillna로 nan값 0으로
data_perod = pd.read_csv("동해바다_파주기_통합본.csv", encoding='cp949')
data_perod = data_perod.fillna(0)
data_height = pd.read_csv("동해바다_유의파고_통합본.csv", encoding='cp949')
data_height = data_height.fillna(0)
data_perod['일시'] = pd.to_datetime(data_perod['일시'])
data_height['일시'] = pd.to_datetime(data_height['일시'])


### 울릉도를 예시로, 지그재그 형태의 그래프 그리기
intercept = 0
for j in range(8705, alldata.shape[0] - 14):    
    for i in range(j , j + 14):
        intercept += (themax - data_perod['울릉도'][i])/2
        plt.plot([intercept, intercept + data_perod['울릉도'][i]/4], [0, data_height['울릉도'][i]], color='green')
        plt.plot([intercept + data_perod['울릉도'][i]/4, intercept + (3 * data_perod['울릉도'][i] / 4)], [data_height['울릉도'][i], -1 * data_height['울릉도'][i]], color='green')
        plt.plot([intercept + (3 * data_perod['울릉도'][i] / 4), intercept + data_perod['울릉도'][i]], [-1 * data_height['울릉도'][i],0], color ='green')
        intercept += (themax + data_perod['울릉도'][i])/2
    plt.ylim([-10, 10])
    plt.show(block= False)
    plt.pause(1)
    plt.close()