import requests
import json
import xmltodict

servicekey = "a6jQW+ATBaBB7AO0RCdEwEkq4kqdUcMq4OnSC5MG8oOkjeLNhT0tN17AX5XW/lIyCFAIDjjmY/YhGv+Htjot4Q=="
url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
params ={'serviceKey' : servicekey, 'YM' : '201201', 'NAT_CD' : '112', 'ED_CD' : 'E' }

response = requests.get(url, params=params)
if response.status_code == 200:
    print(response.text)
    result = xmltodict.parse(response.text)
    print(result)
    print(result['response']['body']['items']['item']['natKorNm'])
    jsonData = json.dumps(xmltodict.parse(response.text), indent=4, ensure_ascii=False)
    print(jsonData)
    dict = json.loads(jsonData)
    print(jsonData['response']['body']['items']['item']['natKorNm'])

    #jsonData = json.dumps(xmltodict.parse(response.text), indent=4, ensure_ascii=False)
    #print(jsonData['response']['body']['items']['item']['natKorNm'])
    #jsonData = json.loads(response)
    #if (jsonData['response']['header']['resultMsg'] == 'OK'):
     #   print(json.dumps(jsonData, indent=4,
      #                   sort_keys=True, ensure_ascii=False))