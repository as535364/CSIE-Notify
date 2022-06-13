# CSIE-Notify

## For local development
1. Run `pip install --no-cache-dir -r requirements.txt` (there may be some useless packages such as packages for telegram bot)
2. Read the file crawlers/ntnucsie.py the return value of `get_update` method
3. Coding your own crawlers/yourschoolcrawler.py support `get_update` method
4. Use `python3 test.py` to test your crawler and don't forget to modify the source of the imported `Crawler` class !!!


## For deploy
1.
```bash
git clone https://github.com/as535364/CSIE-Notify
```

2. In src directory `cp .envExample .env` and modify `.env`.

  **Telegram chat id must be an integer.**

  If there are multiple ids, use commas to separate them.

3. 
```bash
docker-compose up -d
```