import pandas as pd
import requests
from bs4 import BeautifulSoup

results = []

for j in range(1, 3):
    print("page: ", j)
    for i in range(11, 17):
        if (i == 12):
            pass
        else:
            url = f'https://www.mcdelivery.co.kr/kr/browse/menu.html?daypartId={j}&catId={i}'

            response = requests.get(url)
            bs = BeautifulSoup(response.content, 'html.parser')
            # product-cards > div > div:nth-child(1)
            menu_list = bs.select('#product-cards > div > div')
            # print(menu_list[4])

            for menu in menu_list:
                # product-cards > div > div:nth-child(1) > div > div.panel-body > h5
                panel_body = menu.find('div', class_='panel-body')
                panel_footer = menu.find('div', class_='panel-footer')
                name = panel_body.find('h5').text
                # product-cards > div > div:nth-child(1) > div > div.panel-footer > div > div.product-info > div > div.product-cost > span
                cost = panel_footer.find('span').text
                cost_str = cost.replace('₩ ', '').replace(',', '')
                cost = int(cost_str)

                # product-cards > div > div:nth-child(1) > div > div.panel-footer > div > div.product-info > div >
                calories = panel_footer.find('div', class_='product-nutritional-info').text.strip()
                allergen_info_list = panel_footer.find('div', class_='popover-wrapper type-sans')
                allergen_info = allergen_info_list.find('div').text.strip()

                print([name, cost, calories, allergen_info])
            print("---------------------------------------------------")

