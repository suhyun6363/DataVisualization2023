from bs4 import BeautifulSoup # html을 parsing하기 편하게하기 위한 parser
import requests
url = 'https://www.subway.co.kr/storeSearch?page=5&rgn1Nm=&rgn2Nm=#storeList'

response = requests.get(url)
decoded_html = response.content.decode('utf-8')
soap = BeautifulSoup(decoded_html, 'html.parser')
tbody = soap.select_one('#storeList > div > div > div.content > table > tbody')
tr_list = tbody.select('tr')
busan_tdlist = tr_list[8].find_all('td')
#print(gangnam_tdlist)
service_list = busan_tdlist[3].find_all('span')
print(service_list)
on_list = busan_tdlist[3].find_all('span', attrs = {'class':'on'})
print(on_list)
#print(service_24)
#print(service_24[1])
#print(service_24[1])
#if(service_list[1].)