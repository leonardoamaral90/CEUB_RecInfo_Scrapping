import datetime
import os
import sys

from src.functions.status import *
from src.functions.logger import *

def save_to_file(data):
    file_name = os.path.basename(__file__)
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_dir = os.path.join(script_dir, '../..', 'data')
        file = os.path.join(file_dir, 'scraped_data.csv')
        
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        
        if not os.path.isfile(file):
            with open(file, "a") as file:
                keys = data[0].keys()
                file.write(f"{';'.join(keys)};date\n")
                
        with open(file, "a") as file:
            for item in data:
                try:
                    file.write(f"{item['full_name']};{item['model']};{item['link']};{item['sku']};{item['brand_name']};{item['weight']};{item['price']};{item['primePrice']};{item['primePriceWithDiscount']};{item['oldPrice']};{item['oldPrimePrice']};{item['priceWithDiscount']};{item['discountPercentage']};{item['rating']};{item['ratingCount']};{item['available']};{item['warranty']};{datetime.datetime.now()}\n")
                except Exception as e:
                    save_log(Status.ERRO.name, e, file_name)
    
    except Exception as e:
        _, _, tb = sys.exc_info()
        
        save_log(Status.ERRO.name, f'Ocorreu um erro na linha [{tb.tb_lineno}]: {e}', file_name)