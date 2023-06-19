from bs4 import BeautifulSoup

url_list = []
with open('big_code_all_strings.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'lxml')
    base = soup.find_all('a')
    for i in base:
        url = i.get('href')
        if url[:6] == '/watch' and url not in url_list:
            url_list.append(url)
with open('video_urls.txt', 'w') as uriki:
    for url1 in url_list:
        uriki.write(f'https://www.youtube.com{url1}\n')
