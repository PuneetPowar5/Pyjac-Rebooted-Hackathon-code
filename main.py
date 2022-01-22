#Resources Used
#https://www.youtube.com/watch?v=gRLHr664tXA
#https://www.youtube.com/watch?v=Bg9r_yLk7VY&t=997s
#https://docs.python-requests.org/en/latest/
#https://www.codegrepper.com/code-examples/python/beautifulsoup+find+all+div+class

import requests
from bs4 import BeautifulSoup


def monitor_item(url):
    data = requests.get(url=url)
    outcome = ''
    parsedData = BeautifulSoup(data.content, 'html.parser')
    if 'newegg' in url:
        tag = parsedData.find_all("div", {"class": "product-inventory"})
        outcome = tag[0].text.strip()[:-1]
    elif 'global.microless.com' in url:
        tag = parsedData.find_all("div", {"class", "instock-lable"})
        outcome = tag[0].text.strip()
    elif 'shopville' in url:
        tag = parsedData.find_all("div", {"class", "product-infor"})
        outcome = tag[0].text.strip()[34:50].strip(' ')
    elif 'canadacomputers' in url:
        tag = parsedData.find_all("div", {"class", "mb-0"})
        outcome = tag[0].text.strip()[:8]
    else:
        tag = parsedData.find_all("div", {"class", "columncontainer"})
        outcome = tag[0].text.strip()[176:187]

    outcome = str(outcome).upper()
    if outcome == 'HURRY, LAST ONE!':
        outcome = 'IN STOCK'
    elif outcome == 'ADD TO CART':
        outcome = 'IN STOCK'
    elif outcome == 'SOLD OUT':
        outcome = 'OUT OF STOCK'
    return outcome
