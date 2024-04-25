import datetime
import os
    
def save_log(type, log, file = None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(script_dir, '../..', 'logs')
    log_file = os.path.join(log_dir, 'log_scrapped.txt')
    
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    if not os.path.isfile(log_file):
        open(log_file, 'a').close()

    with open(log_file, "a") as file:
        if file:
            file.write(f'[{type}][{file}][{datetime.datetime.now()}]: [{log}]\n')
        else:
            file.write(f'[{type}][{datetime.datetime.now()}]: [{log}]\n')