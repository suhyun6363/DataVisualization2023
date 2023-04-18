from bs4 import BeautifulSoup # html을 parsing하기 편하게하기 위한 parser
import requests
import pandas as pd

result = []
count24Store = 0;
countNot24 = 0;

for pageIndex in range(1, 56):
    url = f"https://www.subway.co.kr/storeSearch?page={pageIndex}&rgn1Nm=&rgn2Nm=#storeList"
    response = requests.get(url)
    decoded_html = response.content.decode('utf-8')
    soap = BeautifulSoup(decoded_html, 'html.parser')
    tbody = soap.select_one('#storeList > div > div > div.content > table > tbody')
    tr_list = tbody.select('tr')

    for tr in tr_list:
        td_list = tr.find_all('td')
        storeNum = td_list[0].string
        storeName = td_list[1].text
        storeAddr = td_list[2].text

        service_list = td_list[3].find_all('span', attrs = {'class':'on'})
        breakfast_menu = ''
        service_24hours = 'NO'

        for service in service_list:
            if service.text == '24시간':
                service_24hours = 'YES'
                count24Store = count24Store + 1

        phoneNum = td_list[4].text
        if(phoneNum != 'Coming Soon'):
            print([storeNum, storeName, storeAddr, service_24hours, phoneNum])
            result.append([storeNum, storeName, storeAddr, service_24hours, phoneNum])

#print(len(result))
print("24시간 지원 매장:", count24Store)
countNot24 = len(result) - count24Store
print("지원하지 않는 매장: ", countNot24)

#DataFrame으로 변환 후 CSV로 저장
df = pd.DataFrame(result, columns=('매장번호','매장명','매장주소','24시간서비스','연락처'))
df.to_csv('20210779_Subway.csv', encoding='cp949', index=False)


