from bs4 import BeautifulSoup # html을 parsing하기 편하게하기 위한 parser
import requests     # url 요청에 따른 html 정보 획득
import pandas as pd # 리스트에 담김 데이터를 dataframe으로 변환하기 위해
result = []     # 크롤링 결과를 저장할 리스트 변수 선언

for pageNum in range(0, 500, 20):       # 페이지별 20개 매장만 표시하는 형태라 기본 url을 사용한 전체 page 요청
    # 문자열을 만들기 위한 다양한 방식 중 format 함수 사용
    url = 'http://pncg.co.kr/page/sub3_1.html?offset={page}&se_type=&se_content=&sido=&gugun=&dong=&cs_group=&cs_home=&cs_wi=&cs_kind=&cs_hole='.format(page=pageNum)
    print(url)   # 진행상황 확인용 출력

    response_html = requests.get(url)   # 해당 page 요청
    print(response_html.status_code)    # 정상 유무 확인용 출력 200 이면 ok
    soap = BeautifulSoup(response_html.content.decode('utf-8'), 'html.parser') # response_html.text로 출력했더니 한글이 깨져 강제 decoding

    table = soap.find('table', class_='table_style3 mt30')    # table tag에 'table_style3 mt30'라는 클래스 tag정보 가져옴
    tbody = table.tbody    #  table tag바로 하위에 tbody 테그가 있어 그냥 이렇게 가져옴(하위에 동일 이름 하나만 있을 땐 이렇게 사용하는게 편함)

    #tbody_tag = soap.select('#contents > div > div.sub_contents > div > table > tbody > tr')

    tr_list = tbody.find_all('tr') # tbody하위에 있는 모든 'tr'테크를 list로 반환
    for item in tr_list:           # tr 하나씩 search
        td_list = item.find_all('td')   # tr 하위에 모든 td를 list로 반환
        storeName = td_list[0].strong.get_text() # 리스트 첫번째 요소의 하위 string테그 내 문자열 가져옴
        storeAddr = td_list[1].get_text()        # 리스트 두번째 요소
        storePhone = td_list[2].get_text()       # 리스트 세번째 요소
        storeService = td_list[3].ul.find('img', attrs = {'alt':'단체주문가능'})['src'] #네번째 td 요소 하위 ul 하위 img테그 중 alt 속성이 단체주문가능인 경우 src 속성 정보 가져옴
        storeWorkHour = td_list[4].get_text().strip() # 운영시간 알아왔더니 문자열에 공백있어서 공백 제거
        storeIsOpen = td_list[6].strong.get_text()    # 하위 요소 string의 텍스트 반환
        # 정보 뽑았으니 매장별 취합하여 list에 추가...
        result.append([storeName, storeAddr, storePhone, storeService, storeWorkHour, storeIsOpen])



print(len(result)) # 잘 가져왔는지 수량 파악....
#print(result)
#DataFrame으로 변환 후 CSV로 저장
pandas_type = pd.DataFrame(result, columns=('가맹점명','주소','전화번호','서비스','영업시간','매장상태'))
print(pandas_type)
pandas_type.to_csv('치킨나라_피자공주_매장리스트.csv', encoding='cp949', mode='w', index=True)


# 끝....
