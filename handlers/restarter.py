import os
import zipfile
import wget
import shutil
from pyrogram import Client, filters
from pyrogram.types import Message
from main import SUDOERS


async def restart(message: Message, restart_type):
    if restart_type == "update":
        text = "1"
    else:
        text = "2"
    try:
        await os.execvp(
            "python3",
            [
                "python3",
                "./main.py",
                f"{message.chat.id}",
                f"{message.id}",
                f"{text}",
            ],
        )
    except:
        await os.execvp(
            "python",
            [
                "python",
                "./main.py",
                f"{message.chat.id}",
                f"{message.id}",
                f"{text}",
            ],
        )


# Restart
@Client.on_message(filters.command("restart", ["."]) & filters.me)
@Client.on_message(filters.user(SUDOERS) & filters.command(["restart", "reboot"], [".", "!"]))
async def restart_get(client: Client, message: Message):
    try:
        manjeet = await message.reply_text("**Restarting userbot...**")
        await restart(message, restart_type="restart")
    except:
        await manjeet.edit_text("**An error occured...**")


# Update
@Client.on_message(filters.command('update', ["."]) & filters.user(SUDOERS))
async def update(client: Client, message: Message):
    try:
        await manjeet.edit('**Updating...**')
        link = "https://github.com/kaal0408/Heaven-USERBOT/archive/refs/heads/main.zip"
        wget.download(link, 'temp/archive.zip')

        with zipfile.ZipFile("temp/archive.zip", "r") as zip_ref:
            zip_ref.extractall("temp/")
        os.remove("temp/archive.zip")

        shutil.make_archive("temp/archive", "zip", "temp/FoxUserbot-main/")

        with zipfile.ZipFile("temp/archive.zip", "r") as zip_ref:
            zip_ref.extractall(".")
        os.remove("temp/archive.zip")

        await manjeet.edit('**Userbot succesfully updated\nRestarting...**')
        await restart(message, restart_type="update")
    except:
        await manjeet.edit(f"**An error occured...**")



