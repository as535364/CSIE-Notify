# NTNU-CSIE-Notify
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
