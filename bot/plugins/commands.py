#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG
#PEAKYBOTEVA | @MR-JINN-OF-TG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
import random

PHOTOS = [
    "https://telegra.ph/file/00f3ec42ec504538e8562.jpg",
    "https://telegra.ph/file/c8d504199f35cbef9e7d9.jpg",
    "https://telegra.ph/file/6cde654fda604d8766bfc.jpg",
    "https://telegra.ph/file/842ec4694de82608b18cb.jpg",
    "https://telegra.ph/file/2ab65224486fff9036d60.jpg",
    "https://telegra.ph/file/a1e13e0dee2925389d45d.jpg",
    "https://telegra.ph/file/912e99f6798a3d2b1df23.jpg",
    "https://telegra.ph/file/4c9b2db0dae674721311a.jpg",
    "https://telegra.ph/file/c8d504199f35cbef9e7d9.jpg",
    "https://telegra.ph/file/ce503a23b17d53e630e8f.jpg",
    "https://telegra.ph/file/715f3323eff6db3be2c6a.jpg",
    "https://telegra.ph/file/7060eae48294db4fe794c.jpg",
    "https://telegra.ph/file/260e45cb876f25b1c68ac.jpg",
    "https://telegra.ph/file/99303a13e5327748f6c9e.jpg",
    "https://telegra.ph/file/68eda27d26ade468d8b63.jpg",
    "https://telegra.ph/file/ae952c29c5b6f734cb243.jpg",
    "https://telegra.ph/file/9eb707d924df4f939f404.jpg",
    "https://telegra.ph/file/52174d04e4e8fb6a60c3e.jpg",
]

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🎬 𝙅𝙊𝙄𝙉 🎬', url="https://t.me/ADMOVEI"
                                )
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '🌟 𝙅𝙊𝙄𝙉 🌟', url="https://t.me/ADMOVEIAD"
                                )
                        ] 
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('🕵️‍♂️ 𝘾𝙍𝙀𝘼𝙏𝙊𝙍 🕵️‍♂️', url='https://t.me/Lucifer_Devil_AD'),
        InlineKeyboardButton('⚠️ 𝙂𝙍𝙊𝙐𝙋 ⚠️', url ='https://t.me/ADMOVEIAD')
    ],[
        InlineKeyboardButton('♻️ 𝙅𝙊𝙄𝙉 𝙊𝙐𝙍 𝙈𝘼𝙄𝙉 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ♻️', url='https://t.me/ADMOVEI')
    ],[
        InlineKeyboardButton('💡 𝙃𝙀𝙇𝙋', callback_data="help"),
        InlineKeyboardButton('🔐 𝘾𝙇𝙊𝙎𝙀', callback_data="close")
       ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo=random.choice(PHOTOS),
        caption=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('𝙃𝙊𝙈𝙀 ⚡', callback_data='start'),
        InlineKeyboardButton('𝘼𝘽𝙊𝙐𝙏 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('𝘾𝙇𝙊𝙎𝙀 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
