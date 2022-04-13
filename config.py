# (c) @KenilPatell

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	API_KEY = os.environ.get("API_KEY")
	SERVER_NAME = os.environ.get("SERVER_NAME")
