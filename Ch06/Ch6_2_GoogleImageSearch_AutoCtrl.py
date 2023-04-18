from selenium import webdriver                      # webdriver 사용
from selenium.webdriver.common.keys import Keys     # key 입력을 대신할 놈
from selenium.webdriver.common.by import By         # find_element에서 사용할 놈
from urllib.request import urlretrieve              # url로 이미지 저장
import time                                         # 프로그램 지연...
import os                                           # 파일 경로 생성

SCROLL_PAUSE_SEC = 1                                # 웹페이지에서 스크롤 내리고 데이터 갱신 시간, 인터넷이 느리면 좀 늘리자..

driver = webdriver.Chrome('chromedriver.exe')       # 웹 드라이버 실행
driver.implicitly_wait(10)                          # 페이지 로드되는데 잠시 기다림



driver.get('https://www.google.co.kr/imghp?hl=ko&ogbl') # 구글 이미지 검색 페이지 열기
# .gLFyf 검색창 class
driver.find_element(By.CSS_SELECTOR,'.gLFyf').send_keys('개 닮은 고양이')  # 검색창에 검색어 입력
driver.find_element(By.CSS_SELECTOR,'.gLFyf').send_keys(Keys.RETURN)      # enter 입력


# 스크롤 높이 가져옴
last_height = driver.execute_script("return document.body.scrollHeight")    # 페이지 열렸을 때 스크롤바의 위치
while True:
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 자동으로 스크롤을 맨 아래로 내림 끝까지..
    # 1초 대기
    time.sleep(SCROLL_PAUSE_SEC)                                             # 잠시 기다림
                                                                             # 더 불러올 데이터가 있아면 데이터가 로드되고 스크롤이 맨 아래서 위로 움직임
    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver.execute_script("return document.body.scrollHeight")  # 조금 올라간 스크롤바 높이 저장
    if new_height == last_height:                                            # 같다는 말은 스크롤바가 움직이지 않았다는 것임
        try:
            print('결과 더 보기 버튼이 있냐? 있으면 클릭 클릭 실패하면 예외처리')    # 움직이지 않았다는 것은 더이상 데이터가 없다거나, 더보기 버튼이 생긴 경우임
            # .mye4qd 더보기 class
            driver.find_element(By.CSS_SELECTOR,'.mye4qd').click()           # 버튼이 생겼으면 클릭하고, 클릭 실패하면 예외 처리에 의해 if문 종료
        except:
            print('맨 마지막-데이터가 없음')
            break;

    last_height = new_height


#islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir
image_url_list = driver.find_elements(By.CSS_SELECTOR,'.bRMDJf.islir') #이미지가 포함된 영역 가져옴...

#b = a[0].find_element_by_css_selector('img').get_attribute('src')

file_path = './images'
if not os.path.exists(file_path):
    os.makedirs(file_path)

fileindex = 1

for image_url in image_url_list:            # 검색 결과별 처리....
    url = image_url.find_element(By.CSS_SELECTOR,'img').get_attribute('src') #img 테그에 src 속성을 가져옴. 이게 이미지 url
    filename = str(file_path+f'/{fileindex}.jpg')  # 파일명 지정

    print(filename, fileindex, '번 파일 저장', url)  # 진행상황 출력
    try:
        urlretrieve(str(url), filename)            # src에서 가저온 url을 통해 해당 결로에 이미지 다운로드
    except:
        print(f'{fileindex}번 파일을 저장할 수 없습니다.')
        pass
    fileindex += 1

print('end of program')









