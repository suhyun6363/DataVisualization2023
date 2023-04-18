from bs4 import BeautifulSoup
import requests
import pandas as pd


result = []
for pageIndex in range(0, 481, 20):
    url = f'http://pncg.co.kr/page/sub3_1.html?offset={pageIndex}&se_type=&se_content=&sido=&gugun=&dong=&cs_group=&cs_home=&cs_wi=&cs_kind=&cs_hole='
    response = requests.get(url)
    #print(response.status_code)
    decoded_html = response.content.decode('utf-8')

    soap = BeautifulSoup(decoded_html, 'html.parser')
    #print(soap)
    #print(len(soap.find_all('tbody')))

    #find_tbody = soup.find_all('tbody')
    #print(find_tbody)
    tbody = soap.select_one('#contents > div > div.sub_contents > div > table > tbody')
    #print(tbody)
    #contents > div > div.sub_contents > div > table > tbody
    tr_list = tbody.find_all('tr')
    #print(len(tr_list))
    for tr_item in tr_list:
        td_list = tr_item.find_all('td')
        #print(len(td_list))
        storeName = td_list[0].strong.string
        addr = td_list[1].string
        phoneNum = td_list[2].strong.string
        #print(storeName)
        #print(addr)
        #print(phoneNum)

        #contents > div > div.sub_contents > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > ul > li:nth-child(2) > img
        img = td_list[3].find('img', attrs= {'alt':'홈배달'})
        #print(img['src'])
        #print(td_list[4].div[2].string)
        getWorkHour = td_list[4].get_text() #td_list[4]의 모든 텍스트를 가져와라
        #print(getWorkHour)
        storeIsOpened = td_list[6].strong.string
        #print(storeIsOpened)
        result.append([storeName, addr, phoneNum, getWorkHour, storeIsOpened])


print(result)
print(len(result))

dataframe_type = pd.DataFrame(result, columns= ('가맹점명', '주소', '전화번호', '영업시간', '매장상태'))
dataframe_type.to_csv('피자나라_치킨공주_매장리스트.csv', encoding='cp949', mode='w', index=True)
