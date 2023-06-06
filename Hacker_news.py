import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://news.ycombinator.com/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}
x = 0
while True:
    if x == 0:
        url = 'https://news.ycombinator.com/newest'
    else:
        url = 'https://news.ycombinator.com/newest'+str(new_link)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    base_post = soup.find_all('td', {'class': 'title'})
    for i in base_post:
        item = i.find('a')
        if item is not None and 'github.com' in str(item):
            articles_link = item.get('href')
            print(item.text+articles_link)
            print('='*5)
    nex = soup.find('a', {'class': 'morelink'})
    next_link = nex.get('href')
    new_link = next_link[6:]
    x = x+1
