import telebot as tl

token ="8429480589:AAEYXrAjc1r0DpdEnjoPhoiIwj6utm6UJj8"

bot = tl.TeleBot(token)

@bot.message_handler(commands=['start'])
def responder_start(msg):
    bot.send_message(msg.chat.id, "oi")

while True:
    try:
        print("Bot conectado!")
        bot.polling(none_stop=True)    
    except:
         print("reconectando...")