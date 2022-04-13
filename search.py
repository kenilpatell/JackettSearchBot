import requests
import os
import json
import xml.etree.ElementTree as ET
from pyrogram import Client, filters
from config import Config

bot = Client('pyrogram',
             api_id=Config.API_ID,
             api_hash=Config.API_HASH,
             bot_token=Config.BOT_TOKEN,
             workers=50,
             sleep_threshold=10)

API_KEY = Config.API_KEY
SERVER_NAME = Config.SERVER_NAME

base_url = "https://SERVER/api/v2.0/indexers/all/results/torznab/api?apikey=API_KEY&q="

@bot.on_message(filters.command('start') & filters.private)
def start(bot, message):
    message.reply_text("Hello")

@bot.on_message(filters.command('search') & filters.private)
def search(bot, message):
    query = message.command[1]
    fetch = message.reply_text("**🔍 Searching...**", quote=True)
    endpoint = f"{base_url}{query}&limit=50"
    r = requests.get(endpoint)
    with open('data2.xml', 'w') as fd:
        fd.write(r.text)
    tree = ET.parse("data2.xml")
    root = tree.getroot()
    # print(root.tag)
    list1 = []
    for x in root[0].findall("item"):
        title = x.find('title').text
        indexer = x.find('jackettindexer').text
        link = x.find('link').text
        final = (f"<b>Title:</b> {title}<br><b>Indexer:</b> {indexer}<br><b>Link:</b> {link}\n\n")
        # print(final)
        list1.append(final)
    list1 = '\n'.join(list1)
    url = "https://pasting.ga/api"
    data_json = {"content": str(list1)}
    resp = requests.post(url, json=data_json)
    k = (resp.content)
    f = json.loads(k.decode('utf-8'))
    # print(f.keys())
    code = f['key']
    furl = f"https://pasting.ga/{code}"
    fetch.delete()
    message.reply_text(f"Here Are Top 50 Search Results:\n\n{furl}")
bot.run()
