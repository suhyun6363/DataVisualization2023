from selenium import webdriver                 # pip install selenium 설치 필요
                                               # 2023년 기준 selenium ver.4.x 설치됨
from selenium.webdriver.common.by import By    # 4.x 버전 이후 find_element호출 방식이 변경되어 추가
import time                                    # sleep() 함수 사용을 위해 추가

sleep_duration = 0.1                           # 클릭 이벤트 후 page 변경까지 대기 시간, 중간에 멈추면 이 값을 조금씩 늘려 보자
results = []

driver = webdriver.Chrome('chromedriver.exe')  # 본인이 사용하는 chrome 브라우저 버전에 맞는 chromedriver 다운로드 후 동일 폴더에 저장
#driver.maximize_window()                      # 최대화면 옵션
driver.implicitly_wait(10) #이 driver 객체를 사용하는 코드에서 페이지고 로드되기 까지 최대 10초(정해진 시간만큼) 대기
                           # 10초 이전에 load되면 다음 코드로 바로 진행
url = 'https://www.coffeebeankorea.com/store/store.asp'  # 크롤링할 페이지
driver.get(url)

#지역검색 클릭
region = driver.find_element(By.CSS_SELECTOR, '#region_srh')
region.click()

SiDoBox = driver.find_element(By.CSS_SELECTOR, '#localTitle') #시/도 콤보박스
SiDo_list = driver.find_elements(By.CSS_SELECTOR, '#storeLocal > li')
#driver.find_element(By.CSS_SELECTOR, '#localTitle2').click()
#storeLocal2 > li:nth-child(1) > a
#print(len(GuGun_list))

#storeListUL > li:nth-child(1) > div.store_txt > p.name > span
for SiDo_Item in SiDo_list:
    time.sleep(sleep_duration)
    SiDoBox.click()

    time.sleep(sleep_duration)
    SiDo_Item.click()

    time.sleep(sleep_duration)
    GuGunBox = driver.find_element(By.CSS_SELECTOR, '#localTitle2')
    GuGun_list = driver.find_elements(By.CSS_SELECTOR, '#storeLocal2 > li')

    for GuGun_Item in GuGun_list:
        time.sleep(sleep_duration)
        GuGunBox.click()

        time.sleep(sleep_duration)
        GuGun_Item.click()

        # storeListUL > li
        time.sleep(sleep_duration)
        store_list = driver.find_elements(By.CSS_SELECTOR, '#storeListUL > li')

        for store_item in store_list:
            storeName = store_item.find_element(By.CSS_SELECTOR, 'div.store_txt > p.name > span').text
            store_addr = store_item.find_element(By.CSS_SELECTOR, 'div.store_txt > p.address > span').text

            print([storeName.store_addr])

