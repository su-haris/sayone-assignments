import bs4 as bs

import requests

resp = requests.get('https://www.w3schools.com/xml/simple.xml')
soup = bs.BeautifulSoup(resp.content, 'xml')
# print(soup)

for url in soup.find_all('food'):
    print(url.text)
