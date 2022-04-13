# JackettSearchBot
This is a Telegram Bot written in Python for Searching Over All Indexers Using Jackett API.

# Features:

## By [Kenil](https://github.com/kenilpatell)
- Search Using Jackett API Upto 1000 Queries
- You Can Search On Every Indexers (Added In Jackett) At A Time.


# How to deploy?
## Prerequisites
- Python Installed On Your PC/VPS
- Some Basic Python Knowledge

### 1. Installing requirements

- Clone this repo:
```
git clone https://github.com/kenilpatell/JackettSearchBot JackettSearchBot/ && cd JackettSearchBot
```

- Install dependencies for running setup scripts:
```
pip3 install -r requirements.txt
```

### 2. Editing config.py file

- `API_ID` : This is to authenticate your Telegram account. You can get this from https://my.telegram.org
- `API_HASH` : This is to authenticate your Telegram account. You can get this from https://my.telegram.org
- `BOT_TOKEN` : The Telegram Bot Token that you got from [@BotFather](https://t.me/BotFather)
- `API_KEY` : Jackett's API Key. You Can Get It From Your Jackett Server
- `SERVER_NAME` : You Jackett Domain or IP:PORT

### 3. Running The Bot
- To Run The Bot Use The Below Command
```
python3 search.py
```
### That's It You Can Use Your Bot Now
