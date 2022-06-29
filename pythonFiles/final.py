import os
import pandas as pd 
from datetime import datetime
import warnings
warnings.filterwarnings(action='ignore')

path = './eastseadata/eastseadataRaw/'
# path의 모든 파일 불러오기
file_list = os.listdir(path)
# file_list_py라는 csv파일 형식의 파일 이름들이 들어간 배열 만들기
file_list_py = [file for file in file_list if file.endswith('.csv')]


#id값 딕셔너리 22193:가거도 22298:홍도 del
id_dic = {22297: '가거도', 22103: '거문도', 22104: '거제도', 22101: '덕적도', 22105: '동해', 22107: '마라도', 
        22186: '부안', 22187: '서귀포', 22183: '신안', 22108: '외연도', 21229: '울릉도', 22189: '울산', 22190: '울진', 22185: '인천',
        22184: '추자도', 22102: '칠발도', 22188: '통영', 22106: '포항', 22194: '홍도', 22302: '동해78'}


# 일시와 유의파고 두 열만 있는 판다스 데이터프레임들의 모음 배열 만들기 [ 가거도의 일시/유의파고 데이터프레임, 거문도의 일시/유의파고 데이터프레임, ... ]
# 파일이름에서 id 추출한 리스트 만들기
# dateaframe_list와 id_list에는 같은 인덱스로 한번에 들어간다(append가 같이 있어서)
dataframe_list = []
id_list =[]
for i in file_list_py:
    data = pd.read_csv(path + i, encoding= 'cp949')  
    data = data[['일시', '파향(deg)']]
    data['일시'] = pd.to_datetime(data['일시'])
    dataframe_list.append(data)
    #파일 이름에 있는 코드를 id list라는 배열에 넣음(코드는 _로 구분된 파일 이름의 3번째에)
    string = i.split('_')
    id_list.append(int(string[2]))
dataframe_list_range = len(dataframe_list)
# 지금 데이터프레임의 형식은, 일시 / 파주기의 열 형식으로 되어 있는데, 파주기를 id코드에 따른 딕셔너리 value로 바꿔줌(동해, 울진 등)
for i in range(dataframe_list_range):
    dataframe_list[i].rename(columns={'파향(deg)': '{}'.format(id_dic[id_list[i]])}, inplace = True)

# 하나씩 하나씩 merge해주는 과정 (1,2번쩨 합쳐서 변수에, 다시 그 변수랑 3번째를 합치고, 다시 그거를 4번째랑 합치고...)
a = None
for i in range(dataframe_list_range-1):
    if i == 0:
        a = pd.merge(dataframe_list[i], dataframe_list[i+1], how= 'outer')
    else:
        a = pd.merge(a, dataframe_list[i+1], how= 'outer')
    a = a.sort_values(by='일시')
#하나의 일시가 3번 중복되던 것을 하나로 합쳐주는 함수(매우 중요)
final_dataframe = a.groupby(['일시']).first().reset_index()

#csv파일로 내보내기
final_dataframe.to_csv('./result.csv', encoding='cp949')