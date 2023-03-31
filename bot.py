import telebot

# Токен вашего бота
bot_token = "5922092362:AAHiHnGVIy1GCFR2TkTc4zBn_IG5n1eRrAk"

# Создаем объект бота
bot = telebot.TeleBot(bot_token)

# Обработка сообщений, отправленных боту
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для рассылки сообщений. Чтобы отправить сообщение, введите /send и текст сообщения.")

# Отправка сообщения определенной группе пользователей
@bot.message_handler(commands=['send'])
def send_post(message):
    # Получаем список пользователей, которым нужно отправить сообщение
    users = ['1324653924', 'user2_id', 'user3_id']

    # Отправляем сообщение каждому пользователю из списка
    for user_id in users:
        bot.send_message(user_id, message.text[5:])

# Запускаем бота
bot.polling(none_stop=True)
