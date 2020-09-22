import requests
import json
from bs4 import BeautifulSoup

CSIE_URL = 'https://www.csie.ntnu.edu.tw/index.php/category/announcement/'


class Crawler:
    def __init__(self):
        pass

    def get(self):
        res = requests.get(CSIE_URL)
        news = []
        if res.status_code == requests.codes.ok:
            soup = BeautifulSoup(res.text, 'html.parser')
            news_origin = soup.select('h2.blog-entry-title.entry-title a')
            
            for new in news_origin:
                news.append({'title': new.text, 'link': new['href']})
        else:
            print(res.status_code)

        with open('news.txt', 'w') as f: # update news to news.txt
            json.dump(news, f)

        return news
    
    def get_update(self):
        news = []
        with open('news.txt') as f:
            last_news = json.load(f)
            now_news = self.get()

            for new in now_news:
                if new not in last_news:
                    news.append(new)
        return news