import requests
from my_token import oweather_token
import json


def get_weather():

    params = {'q' : 'Moscow', 'appid' : oweather_token, 'units' : 'Metric', 'lang' : 'ru'}
    req = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    return req.json()

def msc_weather():
    data = get_weather()
    temp = round(data['main']['temp'])
    hum = data['main']['humidity']
    press = round(data['main']['pressure'] / 1.33)
    desc = data['weather'][0]['description']

    return 'Температура в Москве {} C, влажность {} %, давление {} мм рт.ст. {}'.format(temp, hum, press, desc)
'''
with open ('test2.txt', 'w') as f:
    json.dump(get_weather(), f, indent=2, ensure_ascii=False)
'''

print(msc_weather())
 