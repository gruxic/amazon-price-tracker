from bs4 import BeautifulSoup
import requests

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

def price_retriever(website):
    response= requests.get(website,headers=HEADERS)
    soup = BeautifulSoup(response.text,"html.parser")
    price = soup.find(name="span", id="priceblock_dealprice")
    return(price.getText())



