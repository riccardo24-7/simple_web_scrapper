import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/'
params = {'page': 1}
pages = 2
n = 1

while params['page'] <= pages:
    res = requests.get(url, params=params)
    soup = BeautifulSoup(res.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for n, i in enumerate(items, start = n):
        itemName = i.find('h4', class_='card-title').text.strip()
        itemPrice = i.find('h5').text
        print(f'{n}: {itemPrice} for {itemName}')
        
    all_pages = int(soup.find_all('a', class_='page-link')[-2].text)
    pages = all_pages if pages < all_pages else pages
    params['page'] += 1
