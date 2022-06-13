# CSIE-Notify

## For local development
1. Run `pip install --no-cache-dir -r requirements.txt` (there may be some useless packages such as packages for telegram bot)
2. Read the file crawlers/ntnucsiecrawler.py the return value of `get_update` method
3. Coding your own crawlers/yourschoolcrawler.py support `get_update` method
4. Use `python3 test.py` to test your crawler and don't forget to modify the source of the imported `Crawler` class !!!


## For deploy
(TODO: use docker-compose for convenience)
1.
```bash
git clone https://github.com/as535364/NTNU-CSIE-Notify.git
```
2. Modify config.json.
**telegram chat id must be an integer**
3. 
```bash
docker build -t notify .
```
4. 
```bash
docker run -d --name notify notify
```
