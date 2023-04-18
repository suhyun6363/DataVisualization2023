from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

#[CODE 1]
def hollys_store(result):
    for page in range(1,52):
        Hollys_url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store=' %page
        print(Hollys_url)
        html = requests.get(Hollys_url)
        if html.status_code !=200:
            print('status_code : ', html.status_code)
            return

        soupHollys = BeautifulSoup(html.text, 'html.parser')
        tag_tbody = soupHollys.find('tbody')  # 테이블 내 body
        for store in tag_tbody.find_all('tr'):  # tr list 반환
            store_td = store.find_all('td')
            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string
            print([store_name, store_sido, store_address, store_phone])
            result.append([store_name, store_sido, store_address, store_phone])
    return

#[CODE 0]
def main():
    result = []
    print('Hollys store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    hollys_store(result)   #[CODE 1] 호출 
    hollys_tbl = pd.DataFrame(result, columns=('store', 'sido-gu', 'address','phone'))
    hollys_tbl.to_csv('hollys.csv', encoding='cp949', mode='w', index=True)
    del result[:]
       
if __name__ == '__main__':
     main()


