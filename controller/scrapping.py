# 뷰티풀수프와 셀레늄을 활용하여 권한 없는 
# 공공데이터 api 기능 구현하기.
# 속도와 트래픽에서 차이가 있을수 있지만, 방법이 이것 뿐인듯


import requests
from bs4 import BeautifulSoup

url = 'https://www.weather.go.kr/w/obs-climate/sea/buoy.do'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.select('.cont-box03'))
else : 
    print(response.status_code)