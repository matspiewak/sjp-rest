import requests
from bs4 import BeautifulSoup


def is_acceptable(value):
    if "nie występuje w słowniku" in value or "niedopuszczalne w grach" in value:
        return False
    return True


def request_word(word):
    word_raw_data = requests.get(f'https://sjp.pl/{word}')
    word_html = BeautifulSoup(word_raw_data.text, 'html.parser')
    found_word = word_html.find('h1').text.split()[0]
    word_status = word_html.findAll('p')[0].text
    word_data = {
        'word': found_word,
        'acceptable': is_acceptable(word_status),
    }
    return word_data
