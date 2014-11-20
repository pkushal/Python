import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page=1
    while page < max_pages:
        url = 'https://buckysroom.org/trade/search.php?page='+str(page)
        source_code = requests.get(url)  # gets the source code
        plain_text = source_code.text  # extracts the plain text only






