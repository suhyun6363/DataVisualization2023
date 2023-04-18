from bs4 import BeautifulSoup
import requests
import pandas as pd

result = []
recomCount2 = 0
recomCount3 = 0
recomCount4 = 0

url = 'https://www.duksung.ac.kr/univ/majorInfo.do?miIdx=66&menuId=2429'
response = requests.get(url)
decoded_html = response.content.decode('utf-8')
bs = BeautifulSoup(decoded_html, 'html.parser')

#customer_container > div:nth-child(7) > div > table > tbody
table = bs.find('table', class_='tbl text-center')
tbody = table.find('tbody')
tr_list = tbody.select('tr')

for tr in tr_list:
    if(tr == tr_list[len(tr_list) - 1]): break
    td_list = tr.find_all('td')
    grade = td_list[0].text
    category = td_list[1].text
    lecture_name = td_list[2].text

    firstTime = td_list[3].find('span', class_='firstTime').text
    secondTime = td_list[4].find('span', class_='secondTime').text
    if(firstTime == '3') | (secondTime == '3'):
        time = '3'

    note = ''
    if(td_list[6].text == '필수권장'):
        note = '필수권장'
        if(grade == '2'):
            recomCount2 = recomCount2 + 1
        elif (grade == '3'):
            recomCount3 = recomCount3 + 1
        else:
            recomCount4 = recomCount4 + 1

    print([grade, category, lecture_name, time, note])
    result.append([grade, category, lecture_name, time, note])

print("2학년 필수권장과목:", recomCount2)
print("3학년 필수권장과목:", recomCount3)
print("4학년 필수권장과목:", recomCount4)
df = pd.DataFrame(result, columns=('학년','구분','과목명','학점','필수권장유무'))
df.to_csv('20210779_sw.csv', encoding='cp949', index=False)