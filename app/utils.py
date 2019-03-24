import telegram

"""
    some functions to make easier to interact with the
    request data and telegram
"""

def send_telegram_msg(message, chat_id, token):
    """
        Send message to a telegram user or channel
        chat_id -> '@ChannelName'
    """
    bot = telegram.Bot(token=token)
    rq = bot.sendMessage(chat_id=chat_id, text=message)
    return rq.to_json()