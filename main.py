import time
import os
from telegram import Bot


BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
CHAT_ID_MINE = os.getenv('CHAT_ID_MINE')


def main():
    bot = Bot(token=BOT_TOKEN)
    count = 5
    while True:
        try:

            if count >= 30:
                count = 5

            count += 1
            bot.send_message(chat_id=CHAT_ID_MINE, text=f'Have a break for {count} minutes')
            bot.send_message(chat_id=CHAT_ID, text="Wake up")

        except:
            print('Ошибка всего')

        time.sleep(20 * 60)
        print("Hi")





if __name__ == '__main__':
    main()
