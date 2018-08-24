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
	pass

@app.route('/hook', methods=['POST'])
def webhook_handler():
    if request.method == 'POST':
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        chat_id = update.message.chat_id
        text = update.message.text

        bot.sendMessage(chat_id = chat_id, text = text)

    return 'ok'

if __name__ == "__main__":
    _set_webhook()
    app.run()