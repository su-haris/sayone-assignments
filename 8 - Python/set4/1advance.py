import bs4 as bs

import requests

for i in range(0, 25):
    resp = requests.get('http://example.webscraping.com/places/default/index/' + str(i))
    soup = bs.BeautifulSoup(resp.content, 'html.parser')
    # print(soup)

    for url in soup.find_all('td'):
        print(url.text)
        country_link = url.find('img')
        print(country_link.get('src'))

# Crawls through pages till end and displays country name and image link
