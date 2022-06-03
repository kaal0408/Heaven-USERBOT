import logging
from pyrogram import Client, filters, idle
from pyrogram.types import *
import requests
import os
import re
import asyncio
from datetime import datetime
from config import config
from config import *
"from config import SUDO_USERS"
"from config import API_ID"
"from config import API_HASH"
"from config import LOG_GROUP"
"from config import DB_URL"
"from config import ALIVE_IMG"
"from config import MONGO_DB"

from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

API_ID = config.API_ID
API_HASH = config.API_HASH 
LOG_GROUP = config.LOG_GROUP
DB_URL = config.DB_URL
SUDOERS = config.SUDO_USERS
ALIVE_PIC = config.ALIVE_IMG
MONGO_DB = config.MONGO_DB
STRING_SESSION1 = config.STRING_SESSION1
STRING_SESSION2 = config.STRING_SESSION2
STRING_SESSION3 = config.STRING_SESSION3
STRING_SESSION4 = config.STRING_SESSION4
STRING_SESSION5 = config.STRING_SESSION5
if not STRING_SESSION1:
    logging.error("No String Session Found! Exiting!")
    quit(1)

if not API_ID:
    logging.error("No Api-ID Found! Exiting!")
    quit(1)

if not API_HASH:
    logging.error("No ApiHash Found! Exiting!")
    quit(1)

if ALIVE_IMG:
    ALIVE_PIC = config.ALIVE_IMG
else: 
    ALIVE_PIC = 'https://telegra.ph/file/acd5abe21655b9576a279.jpg'

if MONGO_DB:
    MONGO_DB = config.MONGO_DB
else: 
    MONGO_DB = "mongodb+srv://mabma:BlackMamba@cluster0.ok5je.mongodb.net/?retryWrites=true&w=majority"

if LOG_GROUP:
    Owner = LOG_GROUP
else:
    Owner = 777000


if STRING_SESSION1:
    bot1 = Client(session_name= STRING_SESSION1, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot1 = None

if STRING_SESSION2:
    bot2 = Client(session_name= STRING_SESSION2, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot2 = None

if STRING_SESSION3:
    bot3 = Client(session_name= STRING_SESSION3, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot3 = None

if STRING_SESSION4:
    bot4 = Client(session_name= STRING_SESSION4, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot4 = None

if STRING_SESSION5:
    bot5 = Client(session_name= STRING_SESSION5, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot5 = None





scheduler = AsyncIOScheduler()
CMD_HELP = {}
START_TIME = datetime.now()

if bot1:
    bot1.start()
    bot1.join_chat("Murat_30_God")
if bot2:
    bot2.start()
    bot2.join_chat("Murat_30_God")
if bot3:
    bot3.start()
    bot3.join_chat("Murat_30_God")
if bot4:
    bot4.start()
    bot4.join_chat("Murat_30_God")
if bot5:
    bot5.start()
    bot5.join_chat("Murat_30_God")

idle()

print("🎉 Successfully Deployed 🎉 @Murat_30_God")
print("Enjoy! Do visit @Murat_30_God")

