import json
from datetime import datetime, timezone, timedelta

import telebot
from apscheduler.schedulers.blocking import BlockingScheduler

from crawler import Crawler

# Bot setting
TOKEN = ''
CHAT_ID = []

with open('config.json') as f:
    j = json.load(f)
    TOKEN = j['token']
    CHAT_ID = j['chatId']

tb = telebot.TeleBot(TOKEN)


def send_news():
    tz = timezone(timedelta(hours=+8))
    print('Update Time:', datetime.now(tz).isoformat(timespec="seconds"))
    news = Crawler().get_update()
    news_lists = []
    for new in news:
        news_lists.append(f'{new["title"]}\n\n{new["link"]}\n')
    text = '\n\n\n'.join(news_lists)

    for id in CHAT_ID:
        if text:
            tb.send_message(id, text)


if __name__ == '__main__':
    send_news()
    scheduler = BlockingScheduler()
    scheduler.add_job(send_news, 'interval', minutes=5)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
