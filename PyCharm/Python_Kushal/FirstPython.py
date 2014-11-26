import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1

    while page <= max_pages:
        url = 'https://buckysroom.org/trade/search.php?page='+str(page)
        source_code = requests.get(url)  # gets the source code
        plain_text = source_code.text  # extracts the plain text only

        #Now we will convert it into beautiful soup object
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'item-name'}):  # here 'a' is for the links
            href = "https://buckysroom.org"+link.get('href')
            title = link.string
            #print(href)
            #print(title)
            get_single_item_data(href) # here we are going inside each link
        print("outta loop")
        page += 1

def get_single_item_data(item_url):
        source_code = requests.get(item_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for item_name in soup.findAll('div', {'class': 'i-name'}):
            print(item_name.string)  # here we are getting the titles on the given url with class as i-name
        for link in soup.findAll('a'):
            href = "https://buckysroom.org" + link.get('href') # here we are printing all the url links in the same url
            print(href)

def link():
    url = "https://www.thenewboston.com/forum/topic.php?id=2725"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    print("what is this aman")
    for kushal in soup.findAll('div', {'class': 'buckys-bbcode-content'}):
        print(kushal.get)
        aman = soup.findAll('pre')
        print("/n")
        print(aman)

link()
#trade_spider(1)






