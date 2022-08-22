from numpy import block
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import mpld3

from matplotlib.animation import FuncAnimation

alldata = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_파주기_통합본.csv",encoding='cp949')
alldata_height = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_유의파고_통합본.csv" ,encoding='cp949')
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
data_perod = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_파주기_통합본.csv", encoding='cp949')
data_perod = data_perod.fillna(0)
data_height = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_유의파고_통합본.csv", encoding='cp949')
data_height = data_height.fillna(0)
data_perod['일시'] = pd.to_datetime(data_perod['일시'])
data_height['일시'] = pd.to_datetime(data_height['일시'])



def init():
    plt.ylim([-7, 7])
    plt.xlim(0,700)
    return fig,

def animate(i):
    plt.clf()
    plt.ylim([-7, 7])
    plt.xlim([0,700])
    k=0
    for j in range(i+93263, i+93270):
        percentage = data_perod['울릉도'][j]/themax
        x0 = int(100*(1-percentage)/2)+k*100
        x1 = int((100*percentage)/3+x0)
        x2 = int((100*percentage)*2/3+x0)
        x3 = int((100*percentage)+x0)
        
        plt.plot([x0,x1],[0,data_height['울릉도'][j]], color='green')
        plt.plot([x1,x2],[data_height['울릉도'][j],-data_height['울릉도'][j]], color='green')
        plt.plot([x2,x3],[-data_height['울릉도'][j],0], color ='green')
        k+=1


    


fig = plt.gcf()

anim = FuncAnimation(fig=fig, func=animate, init_func=init, interval=1000)

plt.show()
mpld3.show(fig)