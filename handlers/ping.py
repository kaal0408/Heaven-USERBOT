from datetime import datetime
from pyrogram import Client
from pyrogram import filters

@command(pattern="^.ping")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("pong")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("""
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱
┃╰━╯┃╭━━╮╭━━╮╭━━╮
┃╭━━╯┃╭╮┃┃╭╮┃┃╭╮┃
┃┃╱╱╱┃╰╯┃┃┃┃┃┃╰╯┃
╰╯╱╱╱╰━━╯╰╯╰╯╰━╮┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯\n\n
   MY MS → `{ms}`\n  !\n{}".format(ms))
