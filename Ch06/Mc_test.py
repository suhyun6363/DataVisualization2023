from bs4 import BeautifulSoup # html을 parsing하기 편하게하기 위한 parser
import requests
import pandas as pd

result = []
url = 'https://www.mcdonalds.co.kr/kor/store/list.do'
response = requests.get(url)
decoded_html = response.content.decode('utf-8')
soap = BeautifulSoup(decoded_html, 'html.parser')

top_list = soap.select('.depth1 > li')
toStore = top_list[1].a.text

#searchForm > div > fieldset > div > button
form = soap.select('#searchForm > div > fieldset > div')
search = form[0].find('button').text

button_list = soap.select('#container > div.content > div.contArea > div > div > div.mcStore > div > a')
#print(button_list)
num_list = soap.select('#container > div.content > div.contArea > div > div > div.mcStore > div > span > a')
print(num_list)
