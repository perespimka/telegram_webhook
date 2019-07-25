import requests
import re
from random import randint

def get_random_cat():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding':'gzip, deflate',
    'Connection':'keep-alive',
    'DNT':'1'
    }

    request = requests.get('https://www.google.com/search?q=cute+kitten&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjU353X9b7jAhVl5KYKHR3ZBIAQ_AUIESgB&biw=1920&bih=900',
                    headers=headers)

    pics = re.findall(r'"ou":"(https://[\w\d/\-=\?\.]+?.jpg)"', request.text)
    rand_pos = randint(0, len(pics) - 1)
    return pics[rand_pos]
