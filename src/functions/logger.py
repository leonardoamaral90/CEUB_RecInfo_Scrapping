import datetime
import os

def save_log(type, log):
    file_exists = False
    
    file = 'log_scrapped.txt'
    root_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(root_dir, "..", "logs")    
    file_path = os.path.join(data_dir, file)
    
    if os.path.isfile(file_path):
        file_exists = True

    with open("log_scrapped.txt", "a") as file:
        file.write(f'[{type}][{datetime.datetime.now()}]: [{log}]\n')