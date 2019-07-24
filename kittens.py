import requests
import re
from random import randint

def get_random_cat():
    request = requests.get('https://yandex.ru/images/search?text=cute%20kitten')
    pics = re.findall(r',"url":"(https://\S+?.jpg)"}', request.text)
    rand_pos = randint(0, len(pics) - 1)
    return pics[rand_pos]
