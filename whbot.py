from flask import Flask, request
import json
from my_token import token
import requests
from flask_sslify import SSLify
from datetime import datetime
from kittens import get_random_cat

app = Flask(__name__)
sslify = SSLify(app)

'''
def write_js(data, fname='response.json'):
    with open(fname, 'w') as f:
        json.dump(data, f, indent=2)

'''
'''
prox = {'https' :  '195.122.185.95:3128',
        'SOCKS5' : '139.59.169.246:1080'
 }
 '''
greetings = ['привет', 'хай', 'хелло', 'hello', 'hi', 'дратути', 'здравствуй','hey']

class Bot():
    
    def __init__(self, token):
        self.url = 'https://api.telegram.org/bot%s/' % token
        
    
    def send_message(self, chat_id, text):
        params = {'chat_id' : chat_id, 'text' : text}
        meth = 'sendMessage'
        answ = requests.get(self.url + meth, params=params)
        return answ
    def write_log(self, data, fname='logfile.txt'):
        with open(fname, 'a') as f:
            f.write(data + '\n')


my_bot = Bot(token)

@app.route('/')
def index():
    return '<h1>My Telebot</h1>'

@app.route('/shmele', methods=['POST', 'GET'])
def resp():
    if request.method == 'POST':
        r = request.get_json()
        #write_js(r)
        chat_id = r['message']['chat']['id']
        message = r['message']['text']
        time = datetime.fromtimestamp(r['message']['date'])
        user = r['message']['from']['first_name']
        if message.lower() == 'кисик':
            my_bot.send_message(chat_id, get_random_cat())
        elif message.lower() in greetings:
            my_bot.send_message(chat_id, 'Дратути!')
        else:
            my_bot.send_message(chat_id, 'Я не понял(((')
        log_message = 'В {} {} написал(а) {}'.format(time.strftime("%Y-%m-%d %H:%M:%S"), user, message)
        my_bot.write_log(log_message)
        

        return '<h1>wewew</h1>'
    else:
        return '<h1>Вжух</h1>'

if __name__ == "__main__":
    app.run()
