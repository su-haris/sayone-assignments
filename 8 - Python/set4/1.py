import bs4 as bs

import requests

resp = requests.get('http://example.webscraping.com/')
soup = bs.BeautifulSoup(resp.content, 'html.parser')
# print(soup)


for url in soup.find_all('td'):
    print(url.text)
    country_link = url.find('img')
    print(country_link.get('src'))


# for url in soup.find_all('tr'):
#     print(url.text)
