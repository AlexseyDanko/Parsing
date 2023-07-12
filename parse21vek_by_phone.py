import requests
from bs4 import BeautifulSoup
import json
import time
from random import randrange

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.wildberries.by/',
    'Origin': 'https://www.wildberries.by',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}

response = requests.get(
    'https://www.21vek.by/mobile/page:1/?filter[good_status][]=in&filter[sa]=',
    headers=headers,
)
soup = BeautifulSoup(response.content, 'lxml')
base = soup.find('div', {'class': 'b-content'})
articles_links = base.find_all('a', {'class': 'mindbox-pr-view result__link j-ga_track'})
paginator_count = int(soup.find('div', {'class': 'b-tools cr-tools_paginator g-box_lseparator'}).find_all('a')[-2].text)

# articles_urls_list = []
# for page in range(1, paginator_count + 1):
#     response = requests.get(url=f'https://www.21vek.by/mobile/page:{page}/?filter[good_status][]=in&filter[sa]=', headers=headers)
#     soup = BeautifulSoup(response.content, 'lxml')
#
#     articles_urls = soup.find_all('a', {'class': 'mindbox-pr-view result__link j-ga_track'})
#
#     for i in articles_urls:
#         article_url = i.get('href')
#         articles_urls_list.append(article_url)
#     # time.sleep(randrange(1,5))
#     print(f'Processing{page}/{paginator_count}')
#
# with open('articles_urls.txt', 'w') as file:
#     for url in articles_urls_list:
#         file.write(f'{url}\n')

with open('articles_urls.txt') as file:
    urls_list = [line.strip() for line in file.readlines()]
urls_count = len(urls_list)
results_base = []
for u in enumerate(urls_list):
    response = requests.get(url=u[1], headers=headers, )
    soup = BeautifulSoup(response.text, 'lxml')

    phone_title = soup.find('div', {'class': 'content__header'}).find('h1').text.strip()
    img_phone = soup.find('div', {'class': 'l-photo'}).find('div', {'class': 'b-photo', 'id': 'fotorama'}).find(
        'img').get('src')
    price_phone = soup.find('div', {'class': 'item-price'}).find('span',
                                                                 {'class': 'g-price item__price cr-price__in'}).text
    phone_in_stock = soup.find('div', {'class': 'item-price'}).find('span', {
        'class': 'g-status item__status cr-status__in'}).text
    results_base.append({
            'original_url': u[1],
            'phone_title': phone_title,
            'img_phone': img_phone,
            'price_phone': price_phone,
            'phone_in_stock': phone_in_stock,
    })

    print(f'Processing {u[0]+1}/{urls_count}')
with open('results_phone21vek.json', 'w') as file:
    json.dump(results_base, file, indent=4, ensure_ascii=False)
