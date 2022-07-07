import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import os
import math




# file I/O
# data_period = pd.read_csv("../동해바다_파주기_통합본.csv", encoding="cp949")
data_period = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/동해바다_파주기_통합본.csv", encoding="cp949")
data_direction = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/동해바다_파향_통합본.csv", encoding="cp949")


fig = plt.figure(figsize=(15 ,10))
ax = fig.subplots(1, 8, subplot_kw={'projection': 'polar'})


for i in range(93272, len(data_direction)):
    for j in range(i, i+8):
        r_pohang = np.arange(0.001, data_period["포항"][j], 0.01)
        theta_pohang = math.radians(data_direction["포항"][j]) * (r_pohang/r_pohang)        
        ax[j-i].plot(theta_pohang,r_pohang)

        for y in range(8):
            ax[y].set_rmax(30)
            ax[y].set_rticks(np.arange(1, 30, 2))
            ax[y].tick_params(labelsize = 0.0, colors="white")  # Less radial ticks
            ax[y].set_rlabel_position(-22.5)  # Move radial labels away from plotted line
            for z in range(8):
                ax[z].set_title(data_period['일시'][i+z], size = 8)
            ax[y].grid(True)

def init():
    
    return ln,

def update(frame):
    
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),init_func=init, blit=True)
plt.show()