from datetime import datetime
from pyrogram import Client
from pyrogram import filters
from main import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

@Client.on_message(filters.command(["ping", "Ping"], [".", "!"]) & filters.user(SUDOERS))
async def ping(_, message: Message):
    await message.reply_text(f"""⭐ **
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱
┃╰━╯┃╭━━╮╭━━╮╭━━╮
┃╭━━╯┃╭╮┃┃╭╮┃┃╭╮┃
┃┃╱╱╱┃╰╯┃┃┃┃┃┃╰╯┃
╰╯╱╱╱╰━━╯╰╯╰╯╰━╮┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
** ⭐"MY MS → `{ms}`\n  !\n{}".format(ms)""")



 
