import requests
import datetime
import json
import xmltodict
import pandas as pd

servicekey = "a6jQW+ATBaBB7AO0RCdEwEkq4kqdUcMq4OnSC5MG8oOkjeLNhT0tN17AX5XW/lIyCFAIDjjmY/YhGv+Htjot4Q=="
url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getHoliDeInfo'


def getHoliDeInfo(nStartYear, nEndYear):
    jsonResult = []
    result = []
    dataEND = "{0}{1:0>2}".format(str(nEndYear), str(12))  # 데이터 끝 초기화
    isDataEnd = 0  # 데이터 끝 확인용 flag 초기화

    for year in range(nStartYear, nEndYear + 1):
        if (isDataEnd == 1): break  # 데이터 끝 flag 설정되어있으면 작업 중지.
        print("[", year, "]")
        for pageNo in range(1, 4):

            params = {'serviceKey': servicekey, 'pageNo': pageNo, 'numOfRows': '10', 'solYear': year}
            response = requests.get(url, params=params)

            if (response.status_code == 200):
                print("[%s] Url Request Success" % datetime.datetime.now())
                jsonData = json.dumps(xmltodict.parse(response.text), indent=4, ensure_ascii=False)
                dict_type = json.loads(jsonData)
            else:
                print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
                break

            if (dict_type['response']['header']['resultMsg'] == 'NORMAL SERVICE.'):
                # 입력된 범위까지 수집하지 않았지만, 더이상 제공되는 데이터가 없는 마지막 항목인 경우 -------------------
                totalCount = int(dict_type['response']['body']['totalCount'])
                if (totalCount >= 10):
                    if (totalCount % 10 == 0):
                        totalPageNo = totalCount // 10
                    else:
                        totalPageNo = totalCount // 10 + 1
                else:
                    totalPageNo = 1

                if (dict_type['response']['body']['items'] == None) & (pageNo > totalPageNo):
                    print("%s년의 마지막 페이지입니다.\n" % str(year))
                    break
                elif (dict_type['response']['body']['items'] == None) & (pageNo == 1):
                    isDataEnd = 1  # 데이터 끝 flag 설정
                    dataEND = "{0}{1:0>2}".format(str(year - 1), str(12))
                    print("데이터 없음.... \n 제공되는 데이터는 %s년 12월까지입니다."
                          % str(year - 1))
                    break

                # jsonData를 출력하여 확인......................................................
                item = dict_type['response']['body']['items']['item']
                for num in range(0, len(item)):
                    dateName = item[num]['dateName']
                    isHoliday = item[num]['isHoliday']
                    if item[num].get("remarks") != None:
                        remarks = item[num]['remarks']
                    else:
                        remarks = ''
                    locdate = item[num]['locdate']

                    print('[ %s_%s : 공휴일 %s (Y/N) ]' % (locdate, dateName, isHoliday))
                    print('----------------------------------------------------------------------')
                    if item[num].get("remarks") != None:
                        jsonResult.append({'dateName': dateName, 'isHoliday': isHoliday,
                                       'locdate': locdate, 'remarks': remarks})
                        result.append([locdate, dateName, isHoliday, remarks])
                    else:
                        jsonResult.append({'dateName': dateName, 'isHoliday': isHoliday,
                                           'locdate': locdate})
                        result.append([locdate, dateName, isHoliday, remarks])

    return (jsonResult, result, dataEND)


def main():
    print("국경일 및 공휴일 데이터를 수집합니다.")
    nStartYear = int(input('데이터를 몇 년부터 수집할까요? : '))
    nEndYear = int(input('데이터를 몇 년까지 수집할까요? : '))

    jsonResult, result, dataEND = getHoliDeInfo(nStartYear, nEndYear)
    jsonData = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
    print(jsonData)

    # 파일저장 1 : json 파일
    with open('./%s_%d_%s.json' % ('국경일', nStartYear, dataEND), 'w',
              encoding='utf8') as outfile:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(jsonFile)
    # 파일저장 2 : csv 파일
    columns = ["날짜", "명칭", "휴일여부", "비고"]
    result_df = pd.DataFrame(result, columns=columns)
    result_df.to_csv('./%s_%d_%s.csv' % ('국경일', nStartYear, dataEND),
                     index=False, encoding='cp949')


if __name__ == '__main__':
    main()
