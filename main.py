import time

from telegram import Bot


BOT_TOKEN = 'BOT_TOKEN'
CHAT_ID = 'CHAT_ID'


def main():
    bot = Bot(token=BOT_TOKEN)

    while True:
        try:
            bot.send_message(chat_id=CHAT_ID, text='ping from heroku')

        except:
            print('Ошибка всего')

        time.sleep(20 * 60)


if __name__ == '__main__':
    main()