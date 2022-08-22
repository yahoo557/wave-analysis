import numpy as np
import pandas as pd
data_period = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_유의파고_통합본.csv", encoding="cp949")
print(np.linspace(93263, len(data_period), len(data_period),  endpoint=True, dtype='int' ))
       