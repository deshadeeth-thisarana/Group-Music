from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2

MUSICBOT_IMG = "https://telegra.ph/file/423b90ffebdfa598875b0.jpg"

@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo(
        f"""I am an Telegram Groups Music bot 🎶 created by \n[Đ€Ş卄ΔĐ€€Ť卄 Ť卄ĪŞΔŘคŇΔ](t.me/DeshadeethThisarana), I let you play music in your group's voice chat.

The commands I currently support are:

/play - 🎶 Play the replied audio file or YouTube video 
/pause - ▶️ Pause the audio stream 
/resume - ⏸ Resume the audio stream 
/skip - ↪️ Skip the current audio stream
/mute - 🔇 Mute the userbot
/unmute - 🔊 Unmute the userbot
/stop - 🗑🛑 Clear the queue and remove the userbot from the call
        """,
        MUSICBOT_IMG,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/gangoffriends"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/gangoffriendschannel"
                    )
                 ]
                 [   
                     InlineKeyboardButton(
                        "Add me to your group", url="https://t.me/Mr_GroupMusic_bot?startgroup=start" 
                    )
                ]
            ]
        )
    )
