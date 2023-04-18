import pandas as pd
from selenium import webdriver  # webdriver 사용
from selenium.webdriver.common.by import By  # find_elements에서 사용
import time  # 프로그램 지연...

sleep_duration = 0.1  # 클릭 이벤트 후 page 변경까지 대기 시간, 중간에 멈추면 이 값을 조금씩 늘려 보자
result = []

driver = webdriver.Chrome('chromedriver.exe')  # 웹 드라이버 실행
driver.maximize_window()  # 최대화면 옵션
driver.implicitly_wait(10)  # 이 driver 객체를 사용하는 코드에서 페이지고 로드되기 까지 최대 10초(정해진 시간만큼) 대기
# 10초 이전에 load되면 다음 코드로 바로 진행
url = 'https://www.starbucks.co.kr/store/store_map.do'  # 크롤링할 페이지
driver.get(url)  # url open

region = driver.find_element(By.CSS_SELECTOR,
                             '#container > div > form > fieldset > div > section > article.find_store_cont > article > header.loca_search > h3 > a')

sido_list = driver.find_elements(By.CSS_SELECTOR,
                                 '#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li')

def function2():
    str_sido = sido_list[idx].find_element(By.CSS_SELECTOR, 'a').text
    gugun_list = driver.find_elements(By.CSS_SELECTOR, '#mCSB_2_container > ul > li')
    for gugun in gugun_list:
        if (gugun == gugun_list[0]):
            pass
        else:
            str_gugun = gugun.text
            gugun.click()
            time.sleep(sleep_duration)

            store_list = driver.find_elements(By.CSS_SELECTOR, '#mCSB_3_container > ul > li')
            # mCSB_3_container > ul > li:nth-child(1) > strong
            for store in store_list:
                storeName = store.find_element(By.CSS_SELECTOR, 'strong').text
                storeAddr = store.find_element(By.CSS_SELECTOR, 'p').text
                print([str_sido, str_gugun, storeName, storeAddr])
            print(len(store_list), "-------------------------------------------------")
        return store_list

def function(idx, count):
    str_sido = ''
    region.click()
    time.sleep(sleep_duration)
    str_sido = sido_list[idx].find_element(By.CSS_SELECTOR, 'a').text
    sido_list[idx].click()
    time.sleep(sleep_duration)
    str_list = function2()
    function(idx, len(str_list))


idx = 0

function(0, 1)


