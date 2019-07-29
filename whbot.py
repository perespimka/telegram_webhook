from flask import Flask, request
from my_token import token
import requests
from flask_sslify import SSLify
from datetime import datetime
from kittens import get_random_cat
from weather import msc_weather
import re
from translator import translate

app = Flask(__name__)
sslify = SSLify(app)

'''
prox = {'https' :  '195.122.185.95:3128',
        'SOCKS5' : '139.59.169.246:1080'
}
'''
greetings = ['привет', 'хай', 'хелло', 'hello', 'hi', 'дратути', 'здравствуй', 'hey', 'прив', 'здравствуйте', 'приветик']
commands = {'kisik' : get_random_cat, 'weather' : msc_weather}

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
    def check_command(self, text):
        command = re.search(r'/(\w+)', text)
        if command:
            return command.group(1)
        else:
            return None


my_bot = Bot(token)

@app.route('/')
def index():
    return '<h1>My Telebot</h1>'

@app.route('/shmele', methods=['POST', 'GET'])
def resp():
    if request.method == 'POST':
        r = request.get_json()
        
        chat_id = r['message']['chat']['id']
        message = r['message']['text']
        time = datetime.fromtimestamp(r['message']['date'])
        user = r['message']['from']['first_name']
        mess_low = message.lower()
        command = my_bot.check_command(mess_low)
        
        if mess_low in greetings:
            my_bot.send_message(chat_id, 'Дратути!')
        elif mess_low.startswith('/t'):
            if mess_low[2] == ' ':
                my_bot.send_message(chat_id, translate(message[3:]))
            else:
                my_bot.send_message(chat_id, translate(message[2:]))

        elif command in commands:
            my_bot.send_message(chat_id, commands[command]())
        else:
            my_bot.send_message(chat_id, 'Я не понял(((')
        log_message = 'В {} {} написал(а) {}'.format(time.strftime("%Y-%m-%d %H:%M:%S"), user, message)
        my_bot.write_log(log_message)
        return '<h1>wewew</h1>'
    else:
        return '<h1>Вжух</h1>'

if __name__ == "__main__":
    app.run()
