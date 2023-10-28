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
    button1 = types.InlineKeyboardButton("Наш сайт",url='https://take-it.uz/')
    button2 = types.InlineKeyboardButton("Наш Instagram",url='https://instagram.com/take_it_school?igshid=MmU2YjMzNjRlOQ==')
    button3 = types.InlineKeyboardButton("для вопросов АДМИН",url='https://t.me/Take_it_admin')
    # button3 = types.InlineKeyboardButton("Наш сайт",url='https://take-it.uz/')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    msg = """
    Привет я бот Take It 👋.
    Как могу вам помочь ? 😊 
    """
    bot.send_message(message.chat.id,msg,reply_markup=markup)


bot.infinity_polling()
