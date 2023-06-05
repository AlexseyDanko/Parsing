from bs4 import BeautifulSoup
import requests
from time import sleep
import json

cookies = {
    'stopgame': 'ui3bitbailkcud4k3or4ia7ttc',
    'check_live_comments_v3': 'ba5c06745cdb333fee0008bc39f55968feb218733a341e428625d3c289993a7fa^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A22^%^3A^%^22check_live_comments_v3^%^22^%^3Bi^%^3A1^%^3Bs^%^3A19^%^3A^%^222023-06-05^%^2009^%^3A46^%^3A52^%^22^%^3B^%^7D',
    'last_visit_date_v2': 'fd4d3b02fdf9e2183833b6e3c639001b8c001513d7c7435688c3169986180a55a^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A18^%^3A^%^22last_visit_date_v2^%^22^%^3Bi^%^3A1^%^3Bs^%^3A19^%^3A^%^222023-06-05^%^2010^%^3A00^%^3A53^%^22^%^3B^%^7D',
    '_stopgame-csrf': 'd5e30b6ae71d45430db81ffb03b7db80c8b501f33354ae494fbdeaa9de4c0a77a^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A14^%^3A^%^22_stopgame-csrf^%^22^%^3Bi^%^3A1^%^3Bs^%^3A32^%^3A^%^22sJqMX9FnVkJXHOlN4IpQfM-6gomfoFi6^%^22^%^3B^%^7D',
    'sg-color-scheme': 'light',
    '_ga': 'GA1.2.1575305292.1685947613',
    '_gid': 'GA1.2.2132828518.1685947613',
    '_ym_uid': '1685947613132604941',
    '_ym_d': '1685947613',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    '_gat_gtag_UA_2245085_3': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Connection': 'keep-alive',
    # 'Cookie': 'stopgame=ui3bitbailkcud4k3or4ia7ttc; check_live_comments_v3=ba5c06745cdb333fee0008bc39f55968feb218733a341e428625d3c289993a7fa^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A22^%^3A^%^22check_live_comments_v3^%^22^%^3Bi^%^3A1^%^3Bs^%^3A19^%^3A^%^222023-06-05^%^2009^%^3A46^%^3A52^%^22^%^3B^%^7D; last_visit_date_v2=fd4d3b02fdf9e2183833b6e3c639001b8c001513d7c7435688c3169986180a55a^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A18^%^3A^%^22last_visit_date_v2^%^22^%^3Bi^%^3A1^%^3Bs^%^3A19^%^3A^%^222023-06-05^%^2010^%^3A00^%^3A53^%^22^%^3B^%^7D; _stopgame-csrf=d5e30b6ae71d45430db81ffb03b7db80c8b501f33354ae494fbdeaa9de4c0a77a^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A14^%^3A^%^22_stopgame-csrf^%^22^%^3Bi^%^3A1^%^3Bs^%^3A32^%^3A^%^22sJqMX9FnVkJXHOlN4IpQfM-6gomfoFi6^%^22^%^3B^%^7D; sg-color-scheme=light; _ga=GA1.2.1575305292.1685947613; _gid=GA1.2.2132828518.1685947613; _ym_uid=1685947613132604941; _ym_d=1685947613; _ym_isad=2; _ym_visorc=w; _gat_gtag_UA_2245085_3=1',
}
# url_items_list=[]
# for count in range(1,13):
#     response = requests.get('https://stopgame.ru/review/' + 'p' + str(count), cookies=cookies, headers=headers)
#     soup = BeautifulSoup(response.content, 'lxml')
#     items = soup.find_all('article', {'class': '_card_givrd_1 _card--autoheight-mobile_givrd_396'})
#     for item in items:
#         link = item.find('section', {'class': '_card__content_givrd_398'}).find('a', {'class': '_card__title_givrd_1 _card__title--has-subtitle_givrd_1'})
#
#         url_items_list.append('https://stopgame.ru' + link.get('href'))
#         sleep(1)
#     with open('articles_info.txt', 'w') as file:
#         for url in url_items_list:
#             file.write(f'{url}\n')

with open('articles_info.txt') as file:
    urls_list = [line.strip() for line in file.readlines()]

urls_count = len(urls_list)

s = requests.Session()

results_base = []
for url in enumerate(urls_list):
    response = s.get(url=url[1], headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    articles_title = soup.find('div', {'class': '_content-wrapper_t9svi_78 _material-info_t9svi_144'}).find(
        'h1').text.strip()
    articles_date = soup.find('span', {'class': '_date_t9svi_537 _date--full_t9svi_1'}).text.strip()
    articles_author = soup.find('a', {'class': '_author_t9svi_1326'}).find('span').text.strip()
    articles_text = soup.find('div', {'class': '_content_t9svi_8'}).find('p', {
        'class': '_text_t9svi_89 _text-width_t9svi_89'}).text.strip().replace('\n', '')
    results_base.append({
        'original_url': url[1],
        'articles_title': articles_title,
        'articles_date': articles_date,
        'articles_author': articles_author,
        'articles_text': articles_text,

    })
    print(f'Processing {url[0] + 1}/{urls_count}')
codecs = ["cp1252", "cp437", "utf-16be", "utf-16"]
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(results_base, file, indent=4, ensure_ascii=False)
