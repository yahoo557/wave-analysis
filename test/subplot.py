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

print(max(alldata.iloc[2:,2]))
