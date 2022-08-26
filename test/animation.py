import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.dates as mdates
import pandas as pd
import os
import math
import datetime as dt


data_period = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_유의파고_통합본.csv", encoding="cp949")
 
def animate(i):
    dates = data_period["일시"][i+93272:i+93272+10].tolist()
    x = [dt.datetime.strptime(d,'%Y.%m.%d %H:%M') for d in dates]
    y = data_period["동해"][i+93272:i+93272+10].tolist()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y.%m.%d %H:%M'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.cla()
    plt.plot(x,y)

fig, ax = plt.gcf()

ani = FuncAnimation(fig, animate, interval=2000)

plt.tight_layout()
plt.show()
# def init():
#     # 입력받은 기간내의 최대값을 ylim에 넣어야함
#     ax.set_xlim(frame, frame+7)
#     ax.set_ylim(0, 10)
#     return ln,

# def update(frame):
#     



#     ydata = data_period["동해"][frame+93272:frame+93272+7].tolist()
#     # 아래에 꺾은선 그래프 를 그리는 코드가 입력되어야함'
#     # ydata.append(data_period["동해"][frame+93272])
#     ln.set_data(xdata, ydata)
#     return ln,


#frames에는 입력받은 start와 end만 입력하면 순차적으로 들어갈것, 
# ani = FuncAnimation(fig, update, frames=np.linspace(0, len(data_period)-93263, len(data_period)-93263, endpoint=True, dtype='int'),init_func=init, blit=True)
# plt.show()



