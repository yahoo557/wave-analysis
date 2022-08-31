#울릉도, 동해78, 포항 93272부터 동해 78
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd


# r1 = np.arange(0.001, 4, 0.01)
# theta1 = math.radians(60)*(r1/r1)

# r2 = np.arange(0.001, 6, 0.01)
# theta2 = math.radians(120)*(r2/r2)

# fig, ax = plt.subplots(1,3,subplot_kw={'projection': 'polar'})
# ax[0].plot(theta1, r1)
# ax[1].plot(theta2, r2)


# for i in range(3):
#     ax[i].set_rmax(10)
#     ax[i].set_rticks(np.arange(1, 10, 1))  # Less radial ticks
#     ax[i].set_rlabel_position(-22.5)  # Move radial labels away from plotted line
#     ax[i].grid(True)

# plt.subplots_adjust(wspace= 0.5)
# plt.show()

def animate(i):
    return

data_period = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_파주기_통합본.csv", encoding="cp949")
data_direction = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_파향_통합본.csv", encoding="cp949")


for i in range(93272, len(data_direction)):
    fig = plt.figure(figsize=(15 ,10))
    ax = fig.subplots(3, 8, subplot_kw={'projection': 'polar'})
    for j in range(i, i+8):
        r_포항 = np.arange(0.001, data_period["포항"][j], 0.01)
        theta_포항 = math.radians(data_direction["포항"][j]) * (r_포항/r_포항)
        ax[0][j-i].plot(theta_포항,r_포항)

        r_울릉도 = np.arange(0.001, data_period["울릉도"][j], 0.01)
        theta_울릉도 = math.radians(data_direction["울릉도"][j]) * (r_울릉도/r_울릉도)
        ax[1][j - i].plot(theta_울릉도, r_울릉도)

        r_동해78 = np.arange(0.001, data_period["동해78"][j], 0.01)
        theta_동해78 = math.radians(data_direction["동해78"][j]) * (r_동해78/r_동해78)
        ax[2][j - i].plot(theta_동해78, r_동해78)

    for x in range(3):
        for y in range(8):
            ax[x][y].set_rmax(30)
            ax[x][y].set_rticks(np.arange(1, 30, 2))
            ax[x][y].tick_params(labelsize = 0.0, colors="white")  # Less radial ticks
            ax[x][y].set_rlabel_position(-22.5)  # Move radial labels away from plotted line
            for z in range(8):
                ax[x][z].set_title(data_period['일시'][i+z], size = 8)
            ax[x][y].grid(True)
    plt.show(block= False)    
    plt.pause(1)
    plt.close()