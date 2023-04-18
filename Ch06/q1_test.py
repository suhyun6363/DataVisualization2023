from bs4 import BeautifulSoup # html을 parsing하기 편하게하기 위한 parser
import requests

url = "https://www.subway.co.kr/storeSearch?page=11&rgn1Nm=&rgn2Nm=#storeList"
response = requests.get(url)
#print(response.status_code)

decoded_html = response.content.decode('utf-8')
soap = BeautifulSoup(decoded_html, 'html.parser')
#storeList > div > div > div.content > table > tbody
#print(len(soap.find_all('tbody')))

tbody = soap.select_one('#storeList > div > div > div.content > table > tbody')
#print(tbody)
#print(storelist)
#storeList > div > div > div.content > table > tbody > tr:nth-child(1)
#tr = soap.select_one('#storeList > div > div > div.content > table > tbody > tr')
tr = soap.select('div.content > table > tbody > tr')
print(tr)

tr_list = tbody.select('tr') #ver1
#print(tr_list)
#tr_list2 = tbody.find_all('tr') #ver2
#print(tr_list2[0])

td_list = tr_list[4].find_all('td')
storeNum= td_list[0].string
storeName = td_list[1].text #string / get_text()
print(storeName)
storeAddr = td_list[2].a.text
print(storeAddr)
service_list = td_list[3].find_all('span')
phoneNum = td_list[4].div.text
#print(phoneNum)

#td_list2 = tr_list[3].find_all('td')
#phoneNum2 = td_list2[4].div.text
#print(phoneNum2)
#print(service_list)
span_list = td_list[3].find_all('span')
print(span_list)
on_list = td_list[3].find_all('span', attrs = {'class':'on'})
slice_list = on_list[1:]
print(slice_list[1].text)
#print(classOn_list)
#print(service_24)
