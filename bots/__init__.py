from .telebot import TeleBot
from .wxbot import WxBot
from .dingbot import DingBot

def init_bot(bot_token, bot_type, chat_id=None, secret=None):
    if bot_type == 0:
        return WxBot(bot_token)
    elif bot_type == 1:
        return DingBot(bot_token, secret)
    elif bot_type == 2:
        return TeleBot(bot_token, chat_id)

