import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")
que = {}

class config(object):
   SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
   API_ID = int(getenv("API_ID", "6435225"))
   API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
   LOG_GROUP = getenv("LOG_GROUP", "")
   SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")
   SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
   SPOTIFY_USERNAME = getenv("SPOTIFY_USERNAME", "")
   MONGO_DB = getenv("MONGO_DB", "")
   ALIVE_IMG = getenv("ALIVE_IMG", "")
   DB_URL = getenv("DATABASE_URL", "")
   STRING_SESSION1 = getenv("STRING_SESSION1", "")
   STRING_SESSION2 = getenv("STRING_SESSION2", "")
   STRING_SESSION3 = getenv("STRING_SESSION3", "")
   STRING_SESSION4 = getenv("STRING_SESSION4", "")
   STRING_SESSION5 = getenv("STRING_SESSION5", "")

