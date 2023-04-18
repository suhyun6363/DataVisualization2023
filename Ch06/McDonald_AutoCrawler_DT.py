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
url = 'https://www.mcdonalds.co.kr/kor/main.do'  # 크롤링할 페이지
driver.get(url)  # url open

store = driver.find_element(By.CSS_SELECTOR, 'body > div.wrapper > header > div > nav > div > ul > li:nth-child(2) > a')
store.click()
time.sleep(sleep_duration)
search = driver.find_element(By.CSS_SELECTOR, '#searchForm > div > fieldset > div > button')
search.click()
time.sleep(sleep_duration)

page = 0
#dtCount = 0
while(page != 8):
    for i in range(len(num_list)):
        store_list = driver.find_elements(By.CSS_SELECTOR,
                                          '#container > div.content > div.contArea > div > div > div.mcStore > table > tbody > tr')
        # td.tdName > dl > dt > strong
        for store in store_list:
            td_list = store.find_elements(By.CSS_SELECTOR, 'td')
            storeClick = td_list[0].find_element(By.CSS_SELECTOR, 'strong')
            storeClick.click()
            time.sleep(sleep_duration)
            storeName = td_list[0].find_element(By.CSS_SELECTOR, 'strong').text
            storeAddr = td_list[0].find_element(By.CLASS_NAME, 'road').text
            phoneNum = td_list[1].text
            storeTime = td_list[2].text

            service_list = td_list[3].find_elements(By.CSS_SELECTOR, 'div > span')
            #sv = []
            for service in service_list:
                item = service.find_element(By.CSS_SELECTOR, 'label').text.strip()
                if(item == '맥드라이브'):
                    result.append([storeName, storeAddr, phoneNum, storeTime, 'Yes'])
                #sv.append(item)
            ''''
            for item in sv:
                if (item == '맥드라이브'):
                    dtCount += 1
                    print([storeName, storeAddr, phoneNum, storeTime, sv])
                    result.append([storeName, storeAddr, phoneNum, storeTime, sv])
            '''

        button_list = driver.find_elements(By.CSS_SELECTOR,
                                           '#container > div.content > div.contArea > div > div > div.mcStore > div > a')
        num_list = driver.find_elements(By.CSS_SELECTOR,
                                        '#container > div.content > div.contArea > div > div > div.mcStore > div > span > a')
        if (i == len(num_list) - 1):
            button_list[2].click()
            time.sleep(sleep_duration)
            page = page + 1
            break
        else:
            num_list[i+1].click()
            time.sleep(sleep_duration)

#print("DT매장 :", dtCount)
df = pd.DataFrame(result, columns=('매장명', '주소', '전화번호', '영업시간', '맥드라이브'))
dt_df = df[['매장명','맥드라이브']]
print(dt_df)
print("DT 매장 :", dt_df.count())
df.to_csv('맥도날드DT_test.csv', encoding='cp949', index=True)
driver.quit()
