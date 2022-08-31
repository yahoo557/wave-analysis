from numpy import block
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import mpld3
import math
from matplotlib import animation, rc
from IPython.display import HTML
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
data_direction = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_파향_통합본.csv", encoding='cp949')
data_direction = data_direction.fillna(0)
data_perod['일시'] = pd.to_datetime(data_perod['일시'])
data_height['일시'] = pd.to_datetime(data_height['일시'])



def init():
    plt.ylim([-7, 7])
    plt.xlim(0,700)
    return fig,

def animate(i):
    plt.clf()
    tick_x = [50,150,250,350,450,550,650]
    selcetion = ['울릉도', '동해', '동해78', '포항', '울산', '울진']
    date = []
    k=0
    for t in range(5):
        plt.ylim([-7, 7])
        plt.xlim([0,700])
        plt.subplot(5,1,t+1)
    
        
        for j in range(i+93263, i+93270):
            percentage = data_perod[selcetion[t]][j]/themax
            date.append(data_perod['일시'][j])
            x0 = int(100*(1-percentage)/2)+k*100
            x1 = int((100*percentage)/3+x0)
            x2 = int((100*percentage)*2/3+x0)
            x3 = int((100*percentage)+x0)
            plt.plot([x0,x1],[0,data_height[selcetion[t]][j]], color='green')
            plt.plot([x1,x2],[data_height[selcetion[t]][j],-data_height[selcetion[t]][j]], color='green')
            plt.plot([x2,x3],[-data_height[selcetion[t]][j],0], color ='green')
            theta = math.radians(data_direction[selcetion[t]][j])
            plt.annotate('', xy=(tick_x[k]+math.cos(theta), 5+math.sin(theta)), xytext=(tick_x[k],5), arrowprops={'color':'green', 'width':0.05, "headwidth":2})
            
            k+=1
        plt.xticks(tick_x, date, fontsize = 3)

fig = plt.gcf()

anim = FuncAnimation(fig=fig, func=animate, init_func=init, interval=1000)



plt.show()
# rc('animation', html='jshtml')
# rc
# f = open('/Users/seungbaek/Desktop/호텔/파도분석/test/new.txt', 'w')
# f.write(HTML(anim.to_jshtml()).data)
# f.close