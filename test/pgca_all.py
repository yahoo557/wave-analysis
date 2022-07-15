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
# data_period = data_perod.set_index('일시')
data_height = pd.read_csv("동해바다_유의파고_통합본.csv", encoding='cp949')
data_height = data_height.fillna(0)
# data_height = data_height.set_index('일시')
# data_perod['일시'] = pd.to_datetime(data_perod['일시'])
# data_height['일시'] = pd.to_datetime(data_height['일시'])


### 울릉도를 예시로, 지그재그 형태의 그래프 그리기
intercept1 = 0
intercept2 = 0
intercept3 = 0
intercept4 = 0
intercept5 = 0


for j in range(74927, alldata.shape[0] - 14):
    fig = plt.figure(figsize=(30,10))
    date = []
    for i in range(j , j + 7):
        date.append(data_perod["일시"][i])

        plt.subplot(5,1,1)    
        intercept1 += (themax - data_perod['울릉도'][i])/2
        plt.plot([intercept1, intercept1 + data_perod['울릉도'][i]/4], [0, data_height['울릉도'][i]], color='green')
        plt.plot([intercept1 + data_perod['울릉도'][i]/4, intercept1 + (3 * data_perod['울릉도'][i] / 4)], [data_height['울릉도'][i], -1 * data_height['울릉도'][i]], color='green')
        plt.plot([intercept1 + (3 * data_perod['울릉도'][i] / 4), intercept1 + data_perod['울릉도'][i]], [-1 * data_height['울릉도'][i],0], color ='green')
        intercept1 += (themax + data_perod['울릉도'][i])/2
        plt.title("ulreung")
        plt.ylim([-8, 8])
        
        plt.subplot(5,1,2)
        intercept2 += (themax - data_perod['동해'][i])/2
        plt.plot([intercept2, intercept2 + data_perod['동해'][i]/4], [0, data_height['동해'][i]], color='green')
        plt.plot([intercept2 + data_perod['동해'][i]/4, intercept2 + (3 * data_perod['동해'][i] / 4)], [data_height['동해'][i], -1 * data_height['동해'][i]], color='green')
        plt.plot([intercept2 + (3 * data_perod['동해'][i] / 4), intercept2 + data_perod['동해'][i]], [-1 * data_height['동해'][i],0], color ='green')
        intercept2 += (themax + data_perod['동해'][i])/2    
        plt.title("donghae") 
        plt.ylim([-8, 8])

        plt.subplot(5,1,3)   
        intercept3 += (themax - data_perod['울진'][i])/2
        plt.plot([intercept3, intercept3 + data_perod['울진'][i]/4], [0, data_height['울진'][i]], color='green')
        plt.plot([intercept3 + data_perod['울진'][i]/4, intercept3 + (3 * data_perod['울진'][i] / 4)], [data_height['울진'][i], -1 * data_height['울진'][i]], color='green')
        plt.plot([intercept3 + (3 * data_perod['울진'][i] / 4), intercept3 + data_perod['울진'][i]], [-1 * data_height['울진'][i],0], color ='green')
        intercept3 += (themax + data_perod['울진'][i])/2    
        plt.title("ulzin")
        plt.ylim([-8, 8])

        plt.subplot(5,1,4)   
        intercept4 += (themax - data_perod['포항'][i])/2
        plt.plot([intercept4, intercept4 + data_perod['포항'][i]/4], [0, data_height['포항'][i]], color='green')
        plt.plot([intercept4 + data_perod['포항'][i]/4, intercept4 + (3 * data_perod['포항'][i] / 4)], [data_height['포항'][i], -1 * data_height['포항'][i]], color='green')
        plt.plot([intercept4 + (3 * data_perod['포항'][i] / 4), intercept4 + data_perod['포항'][i]], [-1 * data_height['포항'][i],0], color ='green')
        intercept4 += (themax + data_perod['포항'][i])/2    
        plt.title("pohang")
        plt.ylim([-8, 8])
    
        plt.subplot(5,1,5)   
        intercept5 += (themax - data_perod['울산'][i])/2
        plt.plot([intercept5, intercept5 + data_perod['울산'][i]/4], [0, data_height['울산'][i]], color='green')
        plt.plot([intercept5 + data_perod['울산'][i]/4, intercept5 + (3 * data_perod['울산'][i] / 4)], [data_height['울산'][i], -1 * data_height['울산'][i]], color='green')
        plt.plot([intercept5 + (3 * data_perod['울산'][i] / 4), intercept5 + data_perod['울산'][i]], [-1 * data_height['울산'][i],0], color ='green')
        intercept5 += (themax + data_perod['울산'][i])/2    
        plt.title("ulsan")
        plt.xlabel(date, fontdict={'size':4})
        plt.ylim([-8, 8])
       
    
    plt.show(block= False)
    plt.pause(1)
    plt.close()