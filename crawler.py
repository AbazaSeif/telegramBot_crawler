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