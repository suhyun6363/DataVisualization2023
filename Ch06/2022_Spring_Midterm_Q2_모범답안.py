######################################################
# 2022년 1학기 데이터분석 프로그래밍 중간고사 Q2 모범답안
######################################################


from bs4 import BeautifulSoup #HTML parsing을 위해 선언
import requests               #URL 요청 후 HTML 정보 획득을 위해 선언
import pandas as pd           #dataframe(2차원 표 구조) 형태의 자료 구조 사용을 위해 선언

results = []                  #크롤링 결과를 저장할 list 객체

response = requests.get('https://www.duksung.ac.kr/univ/majorInfo.do?miIdx=66&menuId=2429')
#customer_container > div:nth-child(7) > div > table > tbody > tr
if(response.status_code == 200): # url 요청 결과 정상 유무 확인
    soup = BeautifulSoup(response.content, 'html.parser') #응답으로 받은 html 파싱을 위해 bs4 객체로 변환/사용할 parser 지정
    tr_list = soup.select('table.tbl.text-center > tbody > tr') # tr (table row?) tag list 획득
    print(len(tr_list)) # 몇 줄인지 찍어본다...

    for tr_index in range(len(tr_list)-1): # 맨 마지막 줄은 합계임으로 제외시키기 위해 전체 row 수에서 1뺀 횟수 반복
       td_list =  tr_list[tr_index].find_all('td') # tr에 대한 td들 획득

       grade_level =  td_list[0].text   # 학년
       sub_type =  td_list[1].text # 구분
       sub_name =  td_list[2].text # 과목명

       spring_term = td_list[3].find('span') #1학기 정보 중 첫번째 span에 학점이 있어 그냥 find로 가져온다
       credit = spring_term.text # 학점

       if bool(credit) == False:             #1학기에 학점 정보 없는 경우
           fall_term = td_list[4].find('span')  # 2학기 에서 빼온다....
           credit = fall_term.text #학점

       sub_essential =  td_list[6].text #필수과목

        #결과를 list에 누적하여 저장
       results.append([grade_level, sub_type, sub_name, credit, sub_essential])
       #출력해본다...
       print(grade_level, sub_type, sub_name, credit, sub_essential)

    #for문을 다 돌아 results 를 dataframe으로 변환/저장
    df = pd.DataFrame(results, columns=('학년', '구분', '과목명', '학점', '필수권장유무'))


    df = df[['필수권장유무', '학년']] #문제에서 제시한 딱 필요한 부분만 따로 뽑아서 사용하기 위함.
    #필수권장 과목만 따로 추린다...
    print('뽑는 방식1. 특정 column 내 데이터 값의 종류에 따른 수를 알기 위한 value_count 방식')
    print(df[['필수권장유무', '학년']].value_counts())
    print('---------------')

    print('''뽑는 방식2. '필수권장유무' column의 값이 '필수권장'인 행들만 뽑아서 학년으로 group하여 counting ''')
    essential_sub_list = df[df['필수권장유무'] == '필수권장']
    print(essential_sub_list)  ## 필수권장인 항목들만 출력
    print('---------------')
    print(essential_sub_list.groupby(by=['학년']).count())  # 추려진 정보들 중 학년을 그룹핑하여 그룹별로 몇개인지 확인한다...


















