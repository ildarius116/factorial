import telebot
from typing import Any
import sys

sys.set_int_max_str_digits(0)
BOT_TOKEN = "6430286190:AAFeBeVbbR54kwz8JhcLSa-1LfblsiayBMM"
bot = telebot.TeleBot(BOT_TOKEN)
f_cache = {1: 1}


@bot.message_handler(commands=['start'])
def start_message(message: Any) -> None:
    """
    Стартовое сообщение чат бота
    """

    bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}! '
                                           'Привет, Это БОТ для расчета факториала.\n'
                                           'Введи искомое число.\n')


@bot.message_handler(content_types=['text'])
def get_text_messages(message: Any) -> None:
    """
    Принимает на вход сообщение. Если это сообщение является целым числом, то произойдет расчет факториала.
    """

    if message.text == '/start':
        bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}! '
                                               'Привет, Это БОТ для расчета факториала.\n'
                                               'Введи искомое число.\n')
    if message.text.isdigit():
        bot.send_message(message.from_user.id, 'Идет подсчет ...')
        result = factorial(int(message.text))
        if int(message.text) < 1000:
            bot.send_message(message.chat.id, f'Факториал числа "{message.text}" составляет: "{result}"')

        else:
            result = str(result)[-5:]
            # result = result % 100000
            bot.send_message(message.chat.id,
                             f'Факториал числа "{message.text}" составляет (последние 5 цифр): "{result}"')

    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю. Напиши /start.')


def factorial(n):
    for i in range(1, n + 1):
        if i not in f_cache:
            f *= i
            f_cache[i] = f
        else:
            f = f_cache[i]
    return f_cache[n]


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
