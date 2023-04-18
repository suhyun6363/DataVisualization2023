from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

#[CODE 1]
def CoffeeBean_store(result):
    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp" #커피빈 매장 정보 URL
    wd = webdriver.Chrome('chromedriver')                              #제어가능한 chrome 드라이버 객체 생성
             
    for i in range(1, 370):  #매장 수 만큼 반복                          # 매장이 늘었는지 줄었는지 확인할 수 없지만 대량 이정도
        #wd.implicitly_wait(10)                                        # time.sleep()대신 이 코드를 사용하면 최대 1초 기다리고, 페이지  load 되면 다음코드로 진행
        wd.get(CoffeeBean_URL)                                         # Chorme을 통해 url open
        time.sleep(1)  #웹페이지 연결할 동안 1초 대기                      # Webpage가 열릴 때까지 딱 1초만 기다림
        try:
            print("storePop2(%d)" %i)                                  # 진행단계 출력
            wd.execute_script("storePop2(%d)" %i)                      # 자바스크립트 실행
            time.sleep(1) #스크립트 실행 할 동안 1초 대기                  # 자바스크립트가 실행되는 동안 좀 기다림 왜? 페이지 update되야하니까
            html = wd.page_source                                      # page_source updated된 html 문서 받아옴
            soupCB = BeautifulSoup(html, 'html.parser')                # html문서니까 bs4로 변환
            store_name_h2 = soupCB.select("div.store_txt > h2")        # div tag에 store_txt클래스에 h2 tag 선택
            store_name = store_name_h2[0].string                       # 위에서 가저온 tag의 text 읽어옴, .get_text(), .text도 가능
            print(store_name)  #매장 이름 출력하기                        # 진행단계 출력
            store_info = soupCB.select("div.store_txt > table.store_table > tbody > tr > td") # select이기 때문에 tr아래 tdrk 있는 것들은 다 뽑힌다...
            store_address = store_info[2].get_text().strip()           # 주소 얻기 / 텍스트 뒤에 공백이 있어 strip()으로 제거
            #store_address_list = list(store_info[2])
            #store_address = store_address_list[0]
            store_phone = store_info[3].string                         #
            result.append([store_name, store_address, store_phone])    # 리스트 형태로 구성하여 result 리스트에 추가
            print([store_name, store_address, store_phone])
        except:
            print('찾는 매장 없음')
            continue 
    return

#[CODE 0]
def main():
    result = []
    print('CoffeeBean store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    CoffeeBean_store(result)  #[CODE 1]
    
    CB_tbl = pd.DataFrame(result, columns=('store', 'address','phone'))                   #판다스 데이터프레임형태로 변환
    CB_tbl.to_csv('./6장_data/CoffeeBean.csv', encoding='cp949', mode='w', index=True)    #CSV파일로 저장

if __name__ == '__main__':
     main()


#matizCoverLayer0Content > div > div > div.store_txt