import telebot;
bot = telebot.TeleBot('1059383492:AAGcjoTguIlD7y-sGBgyxO0UCIPVE2GgLVU');
from bs4 import BeautifulSoup
import urllib3

from telebot import apihelper

#apihelper.proxy = {'https': 'socks5://166.62.103.159:59526'}


REQUEST_KWARGS={
    'proxy_url': 'socks4://171.103.9.22:4145/',
    # Optional, if you need authentication:
    'urllib3_proxy_kwargs': {
        'assert_hostname': 'False',
        'cert_reqs': 'CERT_NONE'
        # 'username': 'user',
        # 'password': 'password'
    }
}

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "1":
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://192.168.1.49/')
        soup = BeautifulSoup(r.data, "html.parser")
        temp = soup.findAll('', class_="c")

        bot.send_message(message.from_user.id, "hoho")

bot.polling()