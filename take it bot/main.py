import telebot
import config 
from telebot import types
API_TOKEN = config.token

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    f = open("photo.png","rb")
    bot.send_photo(message.chat.id,f)
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("take it",callback_data='1')
    markup.add(button1)
    msg = """
    Привет я бот Take It 👋.
    Как могу вам помоч ? 😊 
    """
    bot.send_message(message.chat.id,msg,reply_markup=markup)

@bot.callback_query_handler(text=['1'])
def swnd_info(message):
    bot.send_message(message.chat.id,'salom')


bot.infinity_polling()