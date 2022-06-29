import os
import re
import pandas as pd 
from datetime import timedelta
from datetime import datetime
from functools import reduce


path = './rawdata/'
# path의 모든 파일 불러오기
file_list = os.listdir(path)
# file_list_py라는 csv파일 형식의 파일 이름들이 들어간 배열 만들기
file_list_py = [file for file in file_list if file.endswith('.csv')]


#id값 딕셔너리 22193 22298 del
id_dic = {22297: '가거도', 22103: '거문도', 22104: '거제도', 22101: '덕적도', 22105: '동해', 22107: '마라도', 
        22186: '부안', 22187: '서귀포', 22183: '신안', 22108: '외연도', 21229: '울릉도', 22189: '울산', 22190: '울진', 22185: '인천',
        22184: '추자도', 22102: '칠발도', 22188: '통영', 22106: '포항', 22194: '홍도'}


# 일시와 유의파고 두 열만 있는 판다스 데이터프레임들의 모음 배열 만들기 [ 가거도의 일시/유의파고 데이터프레임, 거문도의 일시/유의파고 데이터프레임, ... ]
# 파일이름에서 id 추출한 리스트 만들기
# dateaframe_list와 id_list에는 같은 인덱스로 한번에 들어간다(append가 같이 있어서)
dataframe_list = []
id_list =[]
for i in file_list_py:
    data = pd.read_csv(path + i, encoding= 'cp949')  
    data = data[['일시', '유의파고(m)']]
    data['일시'] = pd.to_datetime(data['일시'])
    dataframe_list.append(data)
    string = i.split('_')
    id_list.append(int(string[2]))
dataframe_list_range = len(dataframe_list)
for i in range(dataframe_list_range):
    dataframe_list[i].rename(columns={'유의파고(m)': '{}'.format(id_dic[id_list[i]])}, inplace = True)



#joining_list의 마지막 값 쓸 예정(1번 2번 합치고.. 그다음 그걸 3번이랑 합치고 그다음 그걸... 마지막에는 모든걸 다합치는게 되는거임)
# joining_list =[]

# for i in range(dataframe_list_range-1):
#     a = None
#     if i == 0:
#         if id_list[i] != id_list[i+1]:
#             a = pd.merge(dataframe_list[i], dataframe_list[i+1], how='outer', left_index=True)            
#         else: a = pd.concat([dataframe_list[i], dataframe_list[i+1]])
#         joining_list.append(a)
#     else:
#         if id_dic[id_list[i]] in joining_list[i-1].columns:
#             a = pd.concat([joining_list[i-1], dataframe_list[i+1]])
#         else: a= pd.merge(joining_list[i-1], dataframe_list[i+1], how='outer', left_index=True)
#         joining_list.append(a)

a= None
for i in range(dataframe_list_range-1):
    if i ==0:
        a = pd.merge(dataframe_list[i], dataframe_list[i+1], how= 'outer')
    else:
        a = pd.merge(a, dataframe_list[i+1], how= 'outer')
    a = a.sort_values(by='일시')

df = a.groupby(['일시']).first().reset_index()
df.to_csv('./result.csv', encoding='cp949')


# //////////////////////////////////////////////////////////////////
# # 날짜만 쭉 있는 데이터프레임 만들기(1시간 간격으로)
# date_list = []
# diffhours = timedelta(hours=1)
# startdate = datetime(2011,1,1,0,0,0)
# while True:
#     date_list.append(startdate)
#     startdate += diffhours
#     if startdate == datetime(2021,1,1,0,0,0): break
# benchmark = pd.DataFrame()
# benchmark['일시'] = date_list
# for i in range(len(dataframe_list)):
#     if id_dic[id_list[i]] in benchmark.columns:
#         continue
#     else: benchmark['{0}'.format(id_dic[id_list[i]])] = None


# ////////////////////////////////////////////////////////////////

# benchmark.to_csv("./data/asd.csv", encoding='cp949')

# # print(benchmark['일시'][0])
# # print(dataframe_list[0]['일시'][0])

# benchmark_range = benchmark.shape[0]
# for i in range(benchmark_range):
#     for j in range(len(dataframe_list)):
#         if benchmark['일시'][i] == dataframe_list[j]['일시'][0]:
#             pd.merge(benchmark, dataframe_list[j], on = '일시')       
#             # for k in range(dataframe_list[j].shape[0]):
#             #     if i + k == benchmark_range: break
#             #     if k == dataframe_list[j].shape[0]: break
#             #     benchmark.at[i+k,'{0}'.format(id_dic[id_list[i]])] = dataframe_list[j]['유의파고(m)'][k]
# #             # benchmark['{0}'.format(id_dic[id_list[j]])] = dataframe_list[j]['유의파고(m)']

# print(benchmark)





### 판다스 데이터프레임의 날짜열의 타입을 datetime으로 변경하는 방법
# geomoondo = pd.read_csv('./data/거문도_2011.csv')
# geomoondo['일시'] = pd.to_datetime(geomoondo['일시'])

### str to datetime
# date_time_obj = datetime.strptime(b, '%Y.%m.%d %H:%M')
# print(type(date_time_obj))