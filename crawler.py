import sys
import telegram
from flask import Flask, request
from bs4 import BeautifulSoup
import requests
import re

app = Flask(__name__)

#bot Token
botToken = '681432558:AAEdVCNPNr4AudRvqwhk1Sqmk2hACHpkgWI'
bot = telegram.Bot(token = botToken)

def _set_webhook():
    status = bot.set_webhook('https://telegram-bot-crawler.herokuapp.com/hook')
    if not status:
        print('Webhook setup failed')
        sys.exit(1) 

@app.route('/hook', methods=['POST'])
def webhook_handler():
    if request.method == 'POST':
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        chat_id = update.message.chat_id
        text = update.message.text

        if text == '/dFitness':
            bot.sendMessage(chat_id = chat_id, text = dcardFitness())
        else:
            bot.sendMessage(chat_id = chat_id, text = text)

    return 'ok'

def dcardFitness():
	url = "https://www.dcard.tw/f/fitness"
    retext = "dcard fitness\n"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    fitnessTitle = soup.find_all('h3', re.compile('PostEntry_title_'))
    fitnessLink = soup.find_all('a', re.compile('PostEntry_root_'))

    for index, (title, link) in enumerate(zip(fitnessTitle[:10], fitnessLink[:10])):  #前10篇
        retext += "{0:2d}. {1}\nhttps://www.dcard.tw{2}\n".format(index + 1, title.text, link.get('href'))
    return retext

if __name__ == "__main__":
    _set_webhook()
    app.run()