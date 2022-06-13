from dotenv import load_dotenv
import os
import time
from datetime import datetime, timezone, timedelta
import schedule

import telebot
from crawlers.nycucs import Crawler

# load bot settings
load_dotenv()
TOKEN = os.getenv('TOKEN')
CHAT_IDS = list(map(int, os.getenv('CHAT_ID').split(',')))
tb = telebot.TeleBot(TOKEN, parse_mode='HTML')


def send_news():
    tz = timezone(timedelta(hours=+8))
    print('Update Time:', datetime.now(tz).isoformat(timespec="seconds"))
    news = Crawler().get_update()
    news_lists = []
    for new in news:
        news_lists.append(f'{new["title"]}\n\n{new["link"]}')
    text = '\n\n\n'.join(news_lists)

    for chat_id in CHAT_IDS:
        if text:
            tb.send_message(chat_id, text)


if __name__ == '__main__':
    if not os.path.exists('news.txt'):
        with open('news.txt', 'w') as f:
            f.write('[]')

    send_news()
    schedule.every(5).minutes.do(send_news)
    while True:
        schedule.run_pending()
        time.sleep(1)
