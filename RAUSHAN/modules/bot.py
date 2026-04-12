import sys
import os
from datetime import datetime
from os import execl, getenv
from telethon import events

# ☠️ Heroku ka kachra hata diya yahan se
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, CMD_HNDLR as hl


# ==========================================
# 🏓 PING COMMAND
# ==========================================
@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS or e.sender_id == OWNER_ID:
        start = datetime.now()
        altron = await e.reply(f"•[ 🍃 𝐌ᴀᴅᴀʀᴀ ᴘᴀᴘᴀ σᴘ 🍃 ]•")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit(f"[🍹] ᴅғѕ вααᴘ кє gυℓαм\n[🏓] ɪᴊᴊᴀт ѕє ʀαниα\n[⚡] αυʀ ᴄнυᴅ ᴊαуαgα иαнɪ тσ\n\n➜ `{mp} ms`")


# ==========================================
# 🔄 REBOOT COMMAND
# ==========================================
@X1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS or e.sender_id == OWNER_ID:
        await e.reply(f"ʀєвσσт ᴅσиє\n[🍷] ʀυк ᴊα 2 мɪи вℓк\n[🫧] ғнɪʀ ᴄнσᴅυgα ѕαвкσ єк єк кαʀкє")
        clients = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]
        for client in clients:
            try:
                await client.disconnect()
            except Exception:
                pass
        execl(sys.executable, sys.executable, *sys.argv)


# ==========================================
# 👑 SUDO COMMAND (Railway Optimized) ☠️
# ==========================================
@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply(f"»🍃 **𝐖єℓᴄσмє тσ ᴅғѕ gαᴅᴅαʀɪ иαнɪ кαʀиα иαнɪ тσ вαᴅмσѕнɪ мα кαʀυgα αυʀ ααᴊ ѕє тυ нαмℓσg кα внαɪ** 🍃")
        
        target = None
        
        # Reply se ID nikalna ya command se
        if event.is_reply:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        else:
            try:
                target = int(event.pattern_match.group(1).strip())
            except ValueError:
                return await ok.edit("αвє ᴊʜᴀᴛ кє вααℓ υραʀ ѕє ʀєᴘℓу ᴅє ʀαнα нαι вααᴘ кσ")

        if target in SUDO_USERS:
            await ok.edit(f"ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !!")
        else:
            # ☠️ MEMORY ME ADD KAR DIYA (Instantly working on Railway)
            SUDO_USERS.append(target)
            await ok.edit(f"»🍃 **нℓσ мєʀα ᴄυтɪєє** 🍃\n:⧽ `{target}`\n:⧽ `ωєℓᴄσмє тσ 𝐒 ᴍ ɢ 〆 ꜱ ᴘ ᴀ ᴍ`")

    elif event.sender_id in SUDO_USERS:
        await event.reply("» ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
