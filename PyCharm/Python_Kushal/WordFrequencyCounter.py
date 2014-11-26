import requests
from  bs4 import BeautifulSoup
import operator

def start(url):
    word_list =[ ]
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)

    for post_text in soup.findAll('a', {'class': 'index_singleListingTitles'}):
        content = post_text.string
        print(content)
        words = content.lower().split()
        for each_words in words:
            word_list.append(each_words)
    clean_Up_List(word_list)

def clean_Up_List (word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_+<>,./?':;-"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i],"") #replaces a symbol with blank space
        if len(word) >0:
            print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(),key = operator.itemgetter(1) ): # operator allows us to work with data types
                   print(key, value)                                                             # 1 for sort by value, 0 for sort by key



start("https://www.thenewboston.com/tops.php?type=text&period=this-month")