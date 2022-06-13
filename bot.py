from dotenv import load_dotenv
import os
from datetime import datetime, timezone, timedelta


import telebot
from apscheduler.schedulers.blocking import BlockingScheduler

from crawlers.ntnucsie import Crawler

# Bot setting
load_dotenv()


tb = telebot.TeleBot(os.getenv('TOKEN'))


def send_news():
    tz = timezone(timedelta(hours=+8))
    print('Update Time:', datetime.now(tz).isoformat(timespec="seconds"))
    news = Crawler().get_update()
    news_lists = []
    for new in news:
        news_lists.append(f'{new["title"]}\n\n{new["link"]}\n')
    text = '\n\n\n'.join(news_lists)

    for chat_id in os.getenv('CHAT_ID').split(','):
        if text:
            tb.send_message(chat_id, text)


if __name__ == '__main__':
    send_news()
    scheduler = BlockingScheduler()
    scheduler.add_job(send_news, 'interval', minutes=5)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
