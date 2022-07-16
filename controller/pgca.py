from numpy import block
import pandas as pd
import matplotlib.pyplot as plt
import time

#파주기, 파향 종합본을 불러와서 nan 값을 0으로 변경한다.
data_period = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_파주기_통합본.csv", encoding='cp949').fillna(0)
data_height = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_유의파고_통합본.csv", encoding='cp949').fillna(0)




#그중 최대값을 찾는다.
temp = 0
for i in range(2,8):
    if temp < max(data_height.iloc[:,i]):
        temp = max(data_height.iloc[:,i]);


for j in range(74927, data_period.shape[0]-14):

    



