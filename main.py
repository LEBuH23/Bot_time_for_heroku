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
            bot.send_message(chat_id=CHAT_ID_MINE, text='Have a break')
            bot.send_message(chat_id=CHAT_ID, text="Wake up")

        except:
            print('Ошибка всего')

        time.sleep(20 * 60)
        print("Hi")





if __name__ == '__main__':
    main()
