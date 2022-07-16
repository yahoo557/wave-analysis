# 뷰티풀수프와 셀레늄을 활용하여 권한 없는 '공공데이터 API' 기능 구현하기.
# 속도와 트래픽에서 차이가 있을수 있지만, 30분 단위로 최신화 할수 있는
# 방법이 이것 뿐인듯 ㅠㅠ
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

driver = set_chrome_driver()

#울릉도, 동해, 동해78, 울진, 포항 해양 기상 부이 30분 마다 스크래핑
url = 'https://www.weather.go.kr/w/obs-climate/sea/buoy.do'
driver.get(url) #잘 동작됨

# 1) 가장 최근의 date를 DB의 가장 최근 date와 비교한다.


# 2) date가 서로 다르다면 data가 갱신된것으로 간주, 스크래핑을 한다.
for i in range (3):
    element = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/table/tbody/tr[1]/td[%d]'% (i+10))
    print(element.get_attribute("innerHTML"))
driver.quit()
# 3) 스크래핑 해온 데이터를 DB에 저장.

# response = requests.get(url)
# if response.status_code == 200:
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#     # print(soup.select('.cont-box03'))

# else : 
#     print(response.status_code)