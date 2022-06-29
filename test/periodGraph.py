import os
import pandas as pd

path ='./eastseadata/동해/'
file_list = os.listdir(path)

dataframe_list =[]
for i in file_list:
    data = pd.read_csv(path + i, encoding= 'cp949')
    data = data[['일시', '파주기(sec)', '유의파고(m)']]
    data['일시'] = pd.to_datetime(data['일시'])
    dataframe_list.append(data)


df_all = pd.concat(dataframe_list, ignore_index=True)
df_all = df_all.sort_values(by= '일시')


print(df_all.shape)