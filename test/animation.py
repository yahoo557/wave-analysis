import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.dates as mdates
import pandas as pd
import os
import math
import datetime as dt

a = [135, 117, 91, 86]
b = [112, 133, 151, 162]
c = [96, 108, 99, 104]
year = ['2018', '2019', '2020', '2021']

df = pd.DataFrame({'shop A' : a, 'shop B' : b, 'shop C' : c}, index = year)
df
import matplotlib.pyplot as plt
import numpy as np

# 그림 사이즈, 바 굵기 조정
fig, ax = plt.subplots(figsize=(12,6))
bar_width = 0.25

# 연도가 4개이므로 0, 1, 2, 3 위치를 기준으로 삼음
index = np.arange(4)

# 각 연도별로 3개 샵의 bar를 순서대로 나타내는 과정, 각 그래프는 0.25의 간격을 두고 그려짐
b1 = plt.plot(index, df['shop A'], bar_width, alpha=0.4, color='red', label='shop A')

b2 = plt.bar(index + bar_width, df['shop B'], bar_width, alpha=0.4, color='blue', label='shop B')

b3 = plt.bar(index + 2 * bar_width, df['shop C'], bar_width, alpha=0.4, color='green', label='shop C')

# x축 위치를 정 가운데로 조정하고 x축의 텍스트를 year 정보와 매칭
plt.xticks(np.arange(bar_width, 4 + bar_width, 1), year)

# x축, y축 이름 및 범례 설정
plt.xlabel('year', size = 13)
plt.ylabel('revenue', size = 13)
plt.legend()
plt.show()
# data_period = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_유의파고_통합본.csv", encoding="cp949")
 
# def animate(i):
#     dates = data_period["일시"][i+93272:i+93272+10].tolist()
#     x = [dt.datetime.strptime(d,'%Y.%m.%d %H:%M') for d in dates]
#     y = data_period["동해"][i+93272:i+93272+10].tolist()
#     plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y.%m.%d %H:%M'))
#     plt.gca().xaxis.set_major_locator(mdates.DayLocator())
#     plt.cla()
#     plt.plot(x,y)

# fig, ax = plt.gcf()

# ani = FuncAnimation(fig, animate, interval=2000)

# plt.tight_layout()
# plt.show()
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



