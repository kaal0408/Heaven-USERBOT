import os
from os import getenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
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
   GROUP_MODE = os.getenv("GROUP_MODE", "True")


contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)

if GROUP_MODE:
    GROUP_MODE = config.GROUP_MODE
else: 
    GROUP_MODE == ("True" or "true")
    grp = True
else:
    grp = False

GRPPLAY = grp
bot1 = Client(STRING_SESSION1, API_ID, API_HASH, plugins=dict(root="handlers"))
call_py = PyTgCalls(bot1)

