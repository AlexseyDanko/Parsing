import requests
from bs4 import BeautifulSoup

cookies = {
    '_ga4s': '1',
    '_ga4': '7332a332-8e9d-43c7-a70f-4aadade8607a',
    '_ga4sid': '1851531179',
    '__gads': 'ID=5320a81f7ff6f64a-22e5ed3e07de00de:T=1686032004:RT=1686035102:S=ALNI_MZktQy8v8Ialp0uZ9jyozJtJKiieA',
    '__gpi': 'UID=00000c43fe2f6861:T=1686032004:RT=1686035102:S=ALNI_MaEIf_xBO1IuXUYTxbBYYqHpK2i2w',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://thehackernews.com/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    # 'Cookie': '_ga4s=1; _ga4=7332a332-8e9d-43c7-a70f-4aadade8607a; _ga4sid=1851531179; __gads=ID=5320a81f7ff6f64a-22e5ed3e07de00de:T=1686032004:RT=1686035102:S=ALNI_MZktQy8v8Ialp0uZ9jyozJtJKiieA; __gpi=UID=00000c43fe2f6861:T=1686032004:RT=1686035102:S=ALNI_MaEIf_xBO1IuXUYTxbBYYqHpK2i2w',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'z': 'JTdCJTIyZXhlY3V0ZWQlMjIlM0ElNUIlNUQlMkMlMjJ0JTIyJTNBJTIyVGhlJTIwSGFja2VyJTIwTmV3cyUyMCU3QyUyMCUyMzElMjBUcnVzdGVkJTIwQ3liZXJzZWN1cml0eSUyME5ld3MlMjBTaXRlJTIyJTJDJTIyeCUyMiUzQTAuNTAxMzE3MjgxMzI4MTYwOSUyQyUyMnclMjIlM0ExOTIwJTJDJTIyaCUyMiUzQTEwODAlMkMlMjJqJTIyJTNBNDI3JTJDJTIyZSUyMiUzQTE5MjAlMkMlMjJsJTIyJTNBJTIyaHR0cHMlM0ElMkYlMkZ0aGVoYWNrZXJuZXdzLmNvbSUyRiUyMiUyQyUyMnIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnd3dy5nb29nbGUuY29tJTJGJTIyJTJDJTIyayUyMiUzQTI0JTJDJTIybiUyMiUzQSUyMlVURi04JTIyJTJDJTIybyUyMiUzQS0xODAlMkMlMjJxJTIyJTNBJTVCJTVEJTdE',
}
count = 0
while True:
    if count == 0:
        url = 'https://thehackernews.com/'
    else:
        url = new_link
    response = requests.get(url, params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    base = soup.find('div', {'class': 'blog-posts clear'})

    articles_link = base.find_all('a', {'class': 'story-link'})
    for urls in articles_link:
        article_link = urls.get('href')
        print(article_link)
    new_link = soup.find('a', {'id': 'Blog1_blog-pager-older-link','class': 'blog-pager-older-link-mobile'}).get('href')
    # print(new_link)
    count = count+1

