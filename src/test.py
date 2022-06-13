import os
import json
from crawlers.nycucs import Crawler

if __name__ == '__main__':
    # init
    try:
        os.remove('news.txt')
    except OSError:
        pass
    with open('news.txt', 'w') as f:
        f.write('[]')

    c = Crawler()

    print(json.dumps(c.get_update(), indent=2, ensure_ascii=False))
