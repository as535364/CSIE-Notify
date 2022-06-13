import requests
import json
from bs4 import BeautifulSoup

CSIE_URL = 'https://www.cs.nycu.edu.tw/announcements'


class Crawler:
    def __init__(self):
        pass

    def get_update(self):
        news = []
        with open('news.txt') as f:
            last_news = json.load(f)
            now_news = self.get()

            for new in now_news:
                if new not in last_news:
                    news.append(new)
        return news

    @staticmethod
    def get():
        res = requests.get(CSIE_URL)
        news = []
        if res.status_code == requests.codes.ok:
            soup = BeautifulSoup(res.text, 'html.parser')
            news_origin = soup.select('li.announcement-item a')

            for new in news_origin:
                news.append({'title': new.text.strip(), 'link': new['href']})
        else:
            print(res.status_code)

        with open('news.txt', 'w') as f:  # update news to news.txt, the titles should be utf-8 encoding
            json.dump(news, f)

        return news
