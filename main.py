import time
import os
from telegram import Bot


BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
CHAT_ID_MINE = os.getenv('CHAT_ID_MINE')

def main():
    bot = Bot(token=BOT_TOKEN)

    while True:
        try:
            bot.send_message(chat_id=CHAT_ID, text='Moscow')
            bot.send_message(chat_id=CHAT_ID_MINE, text='Moscow')
        except:
            print('Ошибка всего')

        time.sleep(25 * 60)


if __name__ == '__main__':
    main()
