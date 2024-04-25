import datetime
import os

from src.functions.status import *
from src.functions.logger import *

def save_to_file(data):
    file_exists = False
    
    file = 'scraped_data.csv'
    root_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(root_dir, "..", "data")    
    file_path = os.path.join(data_dir, file)
    
    if os.path.isfile(file_path):
        file_exists = True
    
    with open("scraped_data.csv", "a") as file:
        if not file_exists:
            keys = data[0].keys()
            file.write(f"{';'.join(keys)};date\n")
            
        for item in data:
            try:
                file.write(f"{item['full_name']};{item['model']};{item['link']};{item['sku']};{item['brand_name']};{item['weight']};{item['price']};{item['primePrice']};{item['primePriceWithDiscount']};{item['oldPrice']};{item['oldPrimePrice']};{item['priceWithDiscount']};{item['discountPercentage']};{item['rating']};{item['ratingCount']};{item['available']};{item['warranty']};{datetime.datetime.now()}\n")
            except Exception as e:
                save_log(Status.ERRO.name, e)