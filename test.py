import os
import json
# from dotenv import load_dotenv
from crawlers.ntnucsie import Crawler


if __name__ == '__main__':
    # init
    try:
        os.remove('news.txt')
    except OSError:
        pass
    with open('news.txt', 'w') as f:
        f.write('[]')

    # load_dotenv()
    # print(os.getenv('TOKEN'), os.getenv('CHAT_ID'))
    c = Crawler()
    
    print(json.dumps(c.get_update(), indent=2, ensure_ascii=False))
