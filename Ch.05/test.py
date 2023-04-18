import requests
import json
import xmltodict
from bs4 import BeautifulSoup

servicekey = "a6jQW+ATBaBB7AO0RCdEwEkq4kqdUcMq4OnSC5MG8oOkjeLNhT0tN17AX5XW/lIyCFAIDjjmY/YhGv+Htjot4Q=="
url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getHoliDeInfo'
params ={'serviceKey' : servicekey, 'pageNo' : '2', 'numOfRows' : '10', 'solYear' : '2024'}

response = requests.get(url, params=params)
result_locdate = []

if response.status_code == 200:
    print(response.text)
    jsonData = json.dumps(xmltodict.parse(response.text), indent=4, ensure_ascii=False)
    print(jsonData)
    dict = json.loads(jsonData)
    print(dict)
    totalCount = dict['response']['body']['totalCount']
    print(totalCount)
    item = dict['response']['body']['items']['item']
    print(item[1])

    for num in range(0, int(totalCount)):
        locdate = item[num]['locdate']
        result_locdate.append(str(locdate))
    print(result_locdate)
