import sys
from datetime import datetime
from os import execl
from telethon import events
from pymongo import MongoClient

# CONFIG
from config import (
    X1, X2, X3, X4, X5, X6, X7, X8, X9, X10,
    OWNER_IDS, OWNER_ID, SUDO_USERS, ENV_SUDO_IDS, CMD_HNDLR as hl, MONGO_URI
)

# ==========================================
# 🍃 MONGODB SETUP
# ==========================================
mongo = MongoClient(MONGO_URI)
db = mongo["DFS_BOT"]
sudo_db = db["SUDO_USERS"]

# Load sudo users from DB and merge with environment-defined sudo users
existing_db_ids = set()
for entry in sudo_db.find():
    try:
        user_id = int(entry.get("user_id"))
    except (TypeError, ValueError):
        continue
    existing_db_ids.add(user_id)
    if user_id not in SUDO_USERS:
        SUDO_USERS.append(user_id)

# Persist Railway env-defined sudo IDs to the DB if they are new
for env_user_id in ENV_SUDO_IDS:
    if env_user_id not in existing_db_ids:
        sudo_db.insert_one({"user_id": env_user_id})
        existing_db_ids.add(env_user_id)

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
# 👑 SUDO ADD (PERMANENT - REPLY ONLY)
# ==========================================
@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo$" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudo$" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudo$" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudo$" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudo$" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudo$" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudo$" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudo$" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudo$" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudo$" % hl))
async def addsudo(event):
    if event.sender_id not in OWNER_IDS:
        return await event.reply("❌ Only owner can add sudo")

    if not event.is_reply:
        return await event.reply("⚠️ Reply to user")

    reply = await event.get_reply_message()
    target = reply.sender_id

    if target in SUDO_USERS:
        return await event.reply("⚠️ Already sudo user")

    # Add to memory
    SUDO_USERS.append(target)

    # Add to MongoDB
    sudo_db.insert_one({"user_id": target})

    await event.reply(f"✅ SUDO ADDED\n👤 `{target}`")

# ==========================================
# ❌ UNSUDO (PERMANENT REMOVE)
# ==========================================
@X1.on(events.NewMessage(incoming=True, pattern=r"\%sunsudo$" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sunsudo$" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sunsudo$" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sunsudo$" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sunsudo$" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sunsudo$" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sunsudo$" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sunsudo$" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sunsudo$" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sunsudo$" % hl))
async def removesudo(event):
    if event.sender_id not in OWNER_IDS:
        return await event.reply("❌ Only owner can remove sudo")

    if not event.is_reply:
        return await event.reply("⚠️ Reply to user")

    reply = await event.get_reply_message()
    target = reply.sender_id

    if target not in SUDO_USERS:
        return await event.reply("⚠️ Not a sudo user")

    # Remove from memory
    SUDO_USERS.remove(target)

    # Remove from MongoDB
    sudo_db.delete_one({"user_id": target})

    await event.reply(f"❌ SUDO REMOVED\n👤 `{target}`")


# ==========================================
# 📋 SHOW SUDO USERS
# ==========================================
@X1.on(events.NewMessage(incoming=True, pattern=r"\%sshowsudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sshowsudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sshowsudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sshowsudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sshowsudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sshowsudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sshowsudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sshowsudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sshowsudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sshowsudo(?: |$)(.*)" % hl))
async def showsudo(event):
    if event.sender_id not in OWNER_IDS:
        return await event.reply("❌ Only owner can use this command")

    users = sorted(set(SUDO_USERS))
    lines = [f"• `{uid}`" for uid in users]
    text = "📌 Current SUDO users:\n" + "\n".join(lines)
    await event.reply(text)


# ==========================================
# 👑 ADD SUDO BY ID
# ==========================================
@X1.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def addsudo_by_id(event):
    if event.sender_id not in OWNER_IDS:
        return await event.reply("❌ Only owner can use this command")

    text = event.text.strip().split(" ", 1)
    if len(text) != 2 or not text[1].strip():
        return await event.reply(f"⚠️ Usage: {hl}addsudo <user_id>")

    try:
        target = int(text[1].strip())
    except ValueError:
        return await event.reply("❌ Invalid user ID")

    if target in SUDO_USERS:
        return await event.reply("⚠️ User is already sudo")

    SUDO_USERS.append(target)
    sudo_db.insert_one({"user_id": target})

    await event.reply(f"✅ SUDO ADDED by ID\n👤 `{target}`")
