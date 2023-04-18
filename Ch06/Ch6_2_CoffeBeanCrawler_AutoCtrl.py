from selenium import webdriver                 # pip install selenium 설치 필요
                                               # 2023년 기준 selenium ver.4.x 설치됨
from selenium.webdriver.common.by import By    # 4.x 버전 이후 find_element호출 방식이 변경되어 추가
import time                                    # sleep() 함수 사용을 위해 추가

sleep_duration = 0.1                           # 클릭 이벤트 후 page 변경까지 대기 시간, 중간에 멈추면 이 값을 조금씩 늘려 보자
results = []

driver = webdriver.Chrome('chromedriver.exe')  # 본인이 사용하는 chrome 브라우저 버전에 맞는 chromedriver 다운로드 후 동일 폴더에 저장
driver.maximize_window()                      # 최대화면 옵션
driver.implicitly_wait(10) #이 driver 객체를 사용하는 코드에서 페이지고 로드되기 까지 최대 10초(정해진 시간만큼) 대기
                           # 10초 이전에 load되면 다음 코드로 바로 진행
url = 'https://www.coffeebeankorea.com/store/store.asp'  # 크롤링할 페이지
driver.get(url)                                          # url open

#region_srh         #:id
#region_srh = driver.find_element_by_css_selector('.region_srh') # 이 방식이 selenium 3.x대 버전
region_srh = driver.find_element(By.CSS_SELECTOR, '#region_srh') #지역검색 버튼이 어디있는지 알아온다 (selenium 4.대버전)
#print(region_srh)
region_srh.click() # 지역검색을 누른다

#localTitle
localTitle = driver.find_element(By.CSS_SELECTOR,'#localTitle') #시/도 콤보박스를 얻어온다
#storeLocal > li:nth-child(1) > a
storeLocal_list = driver.find_elements(By.CSS_SELECTOR, '#storeLocal > li') #시/도 콤보박스 내 시/도(서울, 경기...) 리스트를 얻어온다


for storeLocal in storeLocal_list: #시/도리스트를 하나씩 선택
    time.sleep(sleep_duration)
    localTitle.click() #시/도 콤포박스 클릭
    time.sleep(sleep_duration)
    storeLocal.click() #리스트내 시/도 클릭 순차적

    strSiDo = localTitle.text   #시/도 명 저장

    time.sleep(sleep_duration)
    # localTitle2
    localTitle2 = driver.find_element(By.CSS_SELECTOR,'#localTitle2') #시/도 선택에 따라 구/군 리스트가 생성됨에 따라 얻어옴
    #storeLocal2 > li:nth-child(1)
    storeLocal2_List = driver.find_elements(By.CSS_SELECTOR, '#storeLocal2 > li') # 강남구, 강동구 레벨

    for storeLocal2 in storeLocal2_List: # 구/군 리스트내 정보를 하나씩  클릭하면 가져온다...
        time.sleep(sleep_duration)
        localTitle2.click() #구/군 콤보박스 클릭

        time.sleep(sleep_duration)
        storeLocal2.click() #구/군 내 리스트 순차적으로 클릭

        strGunGoo = localTitle2.text  #시/도 명 저장

        time.sleep(sleep_duration)
        storeListUL = driver.find_elements(By.CSS_SELECTOR, '#storeListUL > li')  # 구/군별 매장 리스트 정보를 얻어온다..

        print('-----------------------------------------------')
        for store_info in storeListUL:    # 구/군별 매장 리스트 원하는 정보를 추출한다.
            # storeListUL > li:nth-child(1) > div.store_txt > p.name > span
            store_name = store_info.find_element(By.CSS_SELECTOR, 'div.store_txt > p.name > span').text   #매장명
            store_addr = store_info.find_element(By.CSS_SELECTOR, 'div.store_txt > p.address > span').text # 주소
            store_tel = store_info.find_element(By.CSS_SELECTOR, 'div.store_txt > p.tel > a').text         #전화번호
            print([strSiDo, strGunGoo, store_name, store_addr, store_tel])                                 #출력해본다

            results.append([strSiDo, strGunGoo, store_name, store_addr, store_tel])

driver.quit() # 크롬 드라이버를 다는다 이 코드가 없어도 본 프로그램이 종료하면 알아서 닫힘

#알아서 저장해보자











