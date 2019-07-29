import requests
from my_token import trans_token

def detect_lang(text):
    params = {'key' : trans_token, 'hint' : 'en,ru', 'text' : text}
    req = requests.post('https://translate.yandex.net/api/v1.5/tr.json/detect', data=params)
    return req.json()['lang']

def translate(text):
    params = {'key' : trans_token, 'lang' : '', 'text' : text}
    lang = detect_lang(text)
    if lang == 'en':
        params['lang'] = 'en-ru'
    elif lang == 'ru':
        params['lang'] = 'ru-en'
    else:
        return 'Язык не определен'
    req = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate', data=params)
    return req.json()['text'][0]

print(translate('hello world'))
