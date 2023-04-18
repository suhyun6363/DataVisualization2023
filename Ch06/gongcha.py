from bs4 import BeautifulSoup
import requests

html_response = requests.get("https://www.gong-cha.co.kr/brand/store/search.php")

if html_response.status_code == 200:
    print(html_response.text)
    bs = BeautifulSoup(html_response.text, 'html.parser')
    bs_tbody = bs.find('tbody')
    #print(bs_tbody)
    bs_tr_list = bs_tbody.find_all('tr')
    #print(bs_tr)
    #print(len(bs_tr))

    for item in bs_tr_list:
        td_list = item.find_all('td')
        for td_item in 
        print(item.find('td'), )