import requests
import json

from bs4 import BeautifulSoup
from urllib.parse import urlparse

from src.functions.status import *
from src.functions.logger import *

headers = {'User-Agent': 'Mozilla/5.0'}

def get_price(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for svg in soup.find_all('svg'):
        svg.extract()
        
    product_info = []
    
    cards = soup.find_all('article', {'class': 'productCard'})
    
    for card in cards:
        product_link = card.find('a', {'class': 'productLink'})['href']
        
        product_info.append({ 'link': product_link })
    
    return product_info

def get_product_info(url, product, x):
    product_info = {}
    try:
        url = f"{url}{product['link']}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        script = soup.find('script', {'type': 'application/ld+json'})
        if script:
            script_text = script.text
            json_data = json.loads(script_text)
            sku = json_data.get('sku')
            brand_name = json_data.get('brand', {}).get('name')

        
        script_nd = soup.find('script', {'type': 'application/json', 'id': '__NEXT_DATA__'})
        if script_nd:
            script_nd_text = script_nd.text
            json_data_nd = json.loads(script_nd_text)
            json_initial = json_data_nd.get('props').get('pageProps').get('initialZustandState').get('descriptionProduct')
            json_catalog_product = json_data_nd.get('props').get('pageProps').get('initialZustandState').get('catalogProduct')
            
            weight = json_catalog_product.get('weight')
            price = json_catalog_product.get('price')
            primePrice = json_catalog_product.get('primePrice')
            primePriceWithDiscount = json_catalog_product.get('primePriceWithDiscount')
            oldPrice = json_catalog_product.get('oldPrice')
            oldPrimePrice = json_catalog_product.get('oldPrimePrice')
            priceWithDiscount = json_catalog_product.get('priceWithDiscount')
            discountPercentage = json_catalog_product.get('discountPercentage')
            rating = json_catalog_product.get('rating')
            ratingCount = json_catalog_product.get('ratingCount')
            available = json_catalog_product.get('available')
            warranty = json_initial.get('warrantyString')
            full_name = json_catalog_product.get('friendlyName')
            
        product_info = {'full_name': full_name,
                        'model': x,
                        'link': url,
                        'sku': sku,
                        'brand_name': brand_name,
                        'weight': weight,
                        'price': price,
                        'primePrice': primePrice,
                        'primePriceWithDiscount': primePriceWithDiscount,
                        'oldPrice': oldPrice,
                        'oldPrimePrice': oldPrimePrice,
                        'priceWithDiscount': priceWithDiscount,
                        'discountPercentage': discountPercentage,
                        'rating': rating,
                        'ratingCount': ratingCount,
                        'available': available,
                        'warranty': warranty}
        
    except Exception as e:
        save_log(Status.ERRO.name, e)

    return product_info

def get_dominio(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc