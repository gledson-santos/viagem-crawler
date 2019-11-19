from src.bd.parametros import Parametros
import telebot


class Telegram(object):

    def __init__(self):
        self.parametros = Parametros()
        self.parametro = self.parametros.retorna_parametros()
        self.bot = telebot.TeleBot(self.parametro['bot_token_telegram'])

    def enviar_msg(self, msg):
        self.bot.send_message(self.parametro['chat_id_telegram'], msg)
