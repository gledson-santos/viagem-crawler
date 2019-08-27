from src.bd.parametros import Parametros
import telebot
import requests


class Telegram(object):

    def __init__(self):
        parametros = Parametros()
        parametro = parametros.retorna_parametros()
        self.request = requests.get("https://api.telegram.org/bot{}/getUpdates".format(parametro['bot_token_telegram'])).json()
        self.chat_id = self.request['result'][0]['message']['chat']['id']
        self.bot = telebot.TeleBot(parametro['bot_token_telegram'])

    def enviar_msg(self, msg):
        self.bot.send_message(self.chat_id, msg)
