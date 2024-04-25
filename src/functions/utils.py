from urllib.parse import urlparse

def get_dominio(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc