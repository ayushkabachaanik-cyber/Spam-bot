from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("ʜєʟᴘ ᴧηᴅ ᴄσϻϻᴧηᴅ", data="help_back")
    ],
    [
        Button.url("υᴘᴅᴀᴛᴇ", "https://t.me/+Imyf3M9TO5k1ODRl"),
        Button.url("sυᴘᴘσʀᴛ", "https://t.me/+dv_rcq5uIXhmMWM1")
    ],
    [
        Button.url("𝐌ᴜꜱɪᴄ ʙᴏᴛ", "https://t.me/RADHA_MUSIC_GMS_op_bot")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        try:
            AltBot = await event.client.get_me()
            bot_name = AltBot.first_name
            bot_id = AltBot.id
            TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
            TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [𝐌 ᴀ ᴅ ᴀ ʀ ᴀ](https://t.me/III_YOUR_MADARA_III)**\n\n"
            TEXT += f"» **xʙᴏᴛꜱ ᴠᴇʀsɪᴏɴ :** `M3.3`\n"
            TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
            TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
            try:
                await event.client.send_file(
                    event.chat_id,
                    "https://d.uguu.se/DUmGrGDy.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
            except Exception:
                await event.client.send_message(
                    event.chat_id,
                    TEXT,
                    buttons=START_BUTTON
                )
        except Exception as e:
            try:
                await event.reply(f"Error: {str(e)[:50]}")
            except Exception:
                pass
