import telebot
import weather
import vksync
from datetime import date

bot = telebot.TeleBot('token')

fa, fb = open('today', 'a'), open('tomorrow', 'a')
fa.close()
fb.close()
today = str(date.today())[8:] 

@bot.message_handler(commands=['start'])
def startMessage(message):
    bot.send_message(message.chat.id, 'Привет, используй /help для справки.')

@bot.message_handler(commands=['help'])
def helpMessage(message):
    bot.send_message(message.chat.id, 'Для получения информации о погоде в твоей местности пришли свою геолокацию.\n\nДля добавления пункта в todo лист пришли сообщение в формате: \"Сегодня(Завтра) *Мероприятие*\".\n\nДля просмотра todo листа пришли сообщение в формате: \"Покажи сегодня(завтра)\".')

@bot.message_handler(commands=['reset'])
def resetFunc(message):
    fa, fb =  open('today', 'w'), open('tomorrow', 'w')
    fa.write('')
    fb.write('')
    fa.close()
    fb.close()
    bot.send_message(message.chat.id, 'Успешно!')

@bot.message_handler(commands=['update'])
def updateNews(message):
    out = vksync.main()
    for i in range(len(out)):
        bot.send_message(message.chat.id, "Обновления из: "+str(out[i][0]))
        for j in range(1, len(out[i])):
            bot.send_message(message.chat.id, out[i][j])
            bot.send_message(message.chat.id, '----------------------')

@bot.message_handler(content_types=['location'])
def location(message):
    bot.send_message(message.chat.id, weather.main(message.location))

@bot.message_handler(content_types=['text'])
def eventMessage(message):
    text = str(message.text.lower())
    if text[0:7] == 'сегодня' and len(text) > 10:
        text = "⚫️ " + text[8].upper() + text[9:] + '\n'
        if today == str(date.today())[8:]:
            fa = open('today', 'a')
            fa.write(text)
            fa.close()
            bot.send_message(message.chat.id, 'Добавлено!')
        else:
            fa, fb = open('today', 'w'), open('tomorrow', 'r')
            tomorrow = fb.read() + text
            fa.write(tomorrow)
            fa.close()
            fb.close()
            fb = open('tomorrow', 'w')
            fb.write('')
            fb.close()
            bot.send_message(message.chat.id, 'Добавлено!')
    elif text[0:6] == 'завтра' and len(text) > 9:
        text = "⚫️ " + text[7].upper() + text[8:] + '\n'
        if today == str(date.today())[8:]:
            fb = open('tomorrow', 'a')
            fb.write(text)
            fb.close()
            bot.send_message(message.chat.id, 'Добавлено!')
        else:
            fa, fb = open('today', 'w'), open('tomorrow', 'r')
            tomorrow = fb.read()
            fa.write(tomorrow)
            fa.close()
            fb.close()
            fb = open('tomorrow', 'w')
            fb.write(text)
            fb.close()
            bot.send_message(message.chat.id, 'Добавлено!')
    elif text[0:8] == 'покажи с':
        fa = open('today', 'r')
        far = fa.read()
        fa.close()
        bot.send_message(message.chat.id, "Список на сегодня:\n" + far)
    elif text[0:8] == 'покажи з':
        fb = open('tomorrow', 'r')
        fbr = fb.read()
        fb.close()
        bot.send_message(message.chat.id, "Список на завтра:\n" + fbr)
    else:
        bot.send_message(message.chat.id, 'Ошибка! /help для справки.')

bot.polling()

