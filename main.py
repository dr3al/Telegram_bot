import telebot
import weather

bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, пришли мне свое местоположение, и я пришлю тебе погоду.')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'погода':
        bot.send_message(message.chat.id, 'Пришли мне свою геоположение')


@bot.message_handler(content_types=['location'])
def location(message):
    bot.send_message(message.chat.id, weather.main(message.location))

bot.polling()