
######################################################
# 2022년 1학기 데이터분석 프로그래밍 중간고사 Q1 모범답안
######################################################
from bs4 import BeautifulSoup #HTML parsing을 위해 선언
import requests               #URL 요청 후 HTML 정보 획득을 위해 선언
import pandas as pd           #dataframe(2차원 표 구조) 형태의 자료 구조 사용을 위해 선언

results = []                  #크롤링 결과를 저장할 list 객체

url = f'https://www.subway.co.kr/storeSearch?page=1&rgn1Nm=&rgn2Nm=#storeList'  # 반복 시 page번호 갱신하여 url 변경

response = requests.get(url)  # 해당 url 요청
soup = BeautifulSoup(response.content, 'html.parser')  # 응답으로 받은 html 파싱을 위해 bs4 객체로 변환/사용할 parser 지정

for pageNum in range(1, 56):  # 매장정보 테이블이 전체 55page로 구성 한 페이지씩 url 요청하기 위함 반복 처리.
    url = f'https://www.subway.co.kr/storeSearch?page={pageNum}&rgn1Nm=&rgn2Nm=#storeList' # 반복 시 page번호 갱신하여 url 변경

    response = requests.get(url) # 해당 url 요청
    print(url)                   # 반복처리되는지 확인하기 위해 프린트문 삽입
    if response.status_code == 200: # url 요청 결과 정상 유무 확인
        soup = BeautifulSoup(response.content, 'html.parser')   #응답으로 받은 html 파싱을 위해 bs4 객체로 변환/사용할 parser 지정
        tr_list = soup.select('div.content > table > tbody > tr') # tr (table row?) tag list 획득

        # storeList > div > div > div.content > table > tbody > tr

        for tr in tr_list:                                        # 각 tr별 처리
            td_list = tr.find_all('td')                           # tr 내 td값 획득
            store_num = td_list[0].text # store_num               # 매장 정보에 대한 text 획득
            store_name = td_list[1].text # store_name             # 매장명 정보에 대한 text 획득
            store_addr =  td_list[2].text # store_addr            # 매장주소 정보에 대한 text 획득
            #store_addr = store_addr.replace('\n', '')             # 앞뒤로 new line 붙어보기 싫으면 제거할 수 있음.
            service_list = td_list[3].find_all('span', class_='on') # 활성화된 서비스 정보 획득

            breakfast_menu = ''
            fullday_service = 'NO'                                 #값 변경용 변수 지정 및 초기값 설정

            for service in service_list:       # 활성화된 서비스 있다면 값 변경
                if service.text == '아침메뉴':  # 그냥 적어봄
                    breakfast_menu = '아침식사 가능 블라블라....'
                elif service.text == '24시간':  # 24시간 활성화 된 경우
                    fullday_service = 'YES'    # yes로 변경

            store_tel = td_list[4].text  # 전화번호 또는 coming soon 정보 획득

            if store_tel != 'Coming Soon': # coming soon이 아닌 경우
                results.append([store_num, store_name, store_addr, fullday_service, store_tel]) #results list에 추가
            else:
                print(f'>>>>>> 매장번호 {store_num} coming soon')
#print(len(results)) #537

#results list를 culumn명 지정하여 pandas dataframe형태로 변환
df = pd.DataFrame(results, columns=('매장번호', '매장명', '매장주소', '24시간서비스', '연락처'))

print(df.groupby('24시간서비스').count()) # pandas groupby 기능 사용하여 24시간서비스 column을 기준으로 그룹화
#또는
fullday_service_store = df[df['24시간서비스']=='YES'] #24시간서비스가 YES인 경우만 추출하여
print('24시간 운영 매장 수 : ', len(fullday_service_store)) # dataframe row 수 출력
print('24시간 운영하지 않는 매장 수 :', df['24시간서비스'].count() - len(fullday_service_store))
print(fullday_service_store) # 확인용 출력



df.to_csv('2021129_Subway.csv', encoding='cp949', index=False) # csv파일로 저장 ms encoding방식인 cp949 세팅

