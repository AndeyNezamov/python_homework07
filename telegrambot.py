import telebot
import random

bot = telebot.TeleBot('6288648913:AAEVm1_BrQSV4bWl95WEltMbQIIQWOu_AeY')


number = random.randint(1,1000)
print(number)
attempts = 0


@bot.message_handler(commands = ['start', 'help'])
def welcome(message):
    global attempts
    attempts = 0
    bot.reply_to(message, 'Поиграем в "Угадай число"?\nЯ загадал число от 1 до 1000, сможешь угадать?! ')

@bot.message_handler(content_types=['text'])
def game_num(message):
    global attempts
    try:
        num_user = int(message.text)
        if number == num_user:
            bot.reply_to(message, f'Ура! Вы победили, количество попыток {attempts}')
            bot.stop_polling()
        elif number > num_user:
            bot.reply_to(message, 'Попробуйте ввести число больше!')
            attempts+=1
        else:
            bot.reply_to(message, 'Попробуйте ввести число меньше!')
            attempts+=1
    except ValueError:
        bot.reply_to(message, 'Некорректный ввод числа!')

bot.polling()
