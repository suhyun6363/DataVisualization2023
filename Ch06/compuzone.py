from bs4 import BeautifulSoup
import requests

html = requests.get('https://smartstore.naver.com/compuzone/category/50003104?cp=1')
#print(html.status_code)
#print(html.text)
bs = BeautifulSoup(html.text, 'html.parser')
ul_list = bs.find_all('ul')
#print(len(ul_list))
ul = bs.find('ul', {'class': 'wOWfwtMC_3 _3cLKMqI7mI _3GwACmAYfW SQUARE'})
#CategoryProducts > ul
#print(ul)
li_list = ul.find_all('li')
for item in li_list:
    price = item.select_one('div > a > div._23DThs7PLJ > strong > span')
    print(price.get_text())
#price = ul.select_one('li > div > a > div._23DThs7PLJ > strong > span')
#print(price.get_text())
#CategoryProducts > ul > li:nth-child(1)첫번째 아이템 > div > a > div._23DThs7PLJ > strong > span                        해당 문장 오른쪽 클릭>copy>copy selector
