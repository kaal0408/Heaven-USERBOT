# Own

from pyrogram.types import Message
import asyncio
import time
from pyrogram import filters, Client
from main import SUDOERS
from main import *

@Client.on_message(filters.me & filters.command(["delspam", "deletespam"], [","]))
@Client.on_message(filters.user(SUDOERS) & filters.command(["delspam", "deletespam"], [","]))
async def delspam(client: Client, message: Message):
    manjeet = await message.reply_text("⚡ Usage:\n /delspam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    await message.delete()
    for i in range(quantity):
        await manjeet.delete()
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.1)
        await msg.delete()
        await asyncio.sleep(0.1)

@Client.on_message(filters.me & filters.command(["spam", "spamming"], [","]))
@Client.on_message(filters.user(SUDOERS) & filters.command(["spam", "spamming"], [","]))
async def suspam(client: Client, message: Message):
    manjeet = await message.reply_text("⚡ Usage:\n /spam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await manjeet.delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.15)


@Client.on_message(filters.me & filters.command(["fastspam"], [","]))
@Client.on_message(filters.user(SUDOERS) & filters.command(["fastspam"], [","]))
async def spspam(client: Client, message: Message):
    manjeet = await message.reply_text("⚡ Usage:\n /fastspam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.002)
        return
    
    for _ in range(quantity):
        await manjeet.delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.002)



@Client.on_message(filters.me & filters.command(["slowspam", "delayspam"], [","]))
@Client.on_message(filters.user(SUDOERS) & filters.command(["slowspam", "delayspam"], [","]))
async def sperm(client: Client, message: Message):
    manjeet = await message.reply_text("⚡ Usage:\n /slowspam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.9)
        return

    for _ in range(quantity):
        await manjeet.delete()
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.9)







@Client.on_message(filters.me & filters.command(["sspam", "stkspam", "spamstk", "stickerspam"], [","]))
@Client.on_message(filters.user(SUDOERS) & filters.command(["sspam", "stkspam", "spamstk", "stickerspam"], [","]))
async def pussy(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit_text("**reply to a sticker with amount you want to spam**")
        return
    if not message.reply_to_message.sticker:
        await message.edit_text(text="**reply to a sticker with amount you want to spam**")
        return
    else:
        i=0
        times = message.command[1]
        if message.chat.type in ["supergroup", "group"]:
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if umm.chat.type == "private":
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id, sticker
                )
                await asyncio.sleep(0.10)






@Client.on_message(filters.command('join', [","]) & filters.me)
@Client.on_message(filters.command('join', [","]) & filters.user(SUDOERS))
async def fuck(client: Client, message: Message):
    manjeet = message.text[6:]
    count = 0
    if not manjeet:
        return await message.reply_text("Need a chat username or invite link to join.")
    if manjeet.isnumeric():
        return await message.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
        await client.join_chat(manjeet)
        await message.reply_text(f"**Joined**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")

@Client.on_message(filters.command('leave', [","]) & filters.me)
@Client.on_message(filters.command('leave', [","]) & filters.user(SUDOERS))
async def leftfuck(client: Client, message: Message):
    manjeet = message.text[6:]
    count = 0
    if not manjeet:
        return await message.reply_text("Need a chat username or invite link to leave.")
    if manjeet.isnumeric():
        return await message.reply_text("Can't leave a chat with chat id. Give username or invite link.")
    try:
        await client.leave_chat(manjeet)
        await message.reply_text(f"**Lefted**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")
