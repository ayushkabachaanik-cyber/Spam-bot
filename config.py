import logging
from telethon import TelegramClient
from os import getenv
from MADARA.data import ALTRON

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

# ==========================================
# ⚙️ BASIC CONFIG
# ==========================================
API_ID = "35411328"
API_HASH = "4c8d3c8f5d3483296f5fb530ea2cfcc6"

MONGO_URI = "mongodb+srv://rj5706603:O95nvJYxapyDHfkw@cluster0.fzmckei.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "cb2147ff-d743-49fc-a18e-6a40aec75e77")

# ==========================================
# 🚂 RAILWAY CONFIG
# ==========================================
RAILWAY_PROJECT_ID = getenv("RAILWAY_PROJECT_ID")
RAILWAY_ENVIRONMENT_ID = getenv("RAILWAY_ENVIRONMENT_ID")
RAILWAY_SERVICE_ID = getenv("RAILWAY_SERVICE_ID")
RAILWAY_STATIC_URL = getenv("RAILWAY_STATIC_URL")
RAILWAY_PROJECT_NAME = getenv("RAILWAY_PROJECT_NAME")
RAILWAY_ENVIRONMENT_NAME = getenv("RAILWAY_ENVIRONMENT_NAME")
RAILWAY_SERVICE_NAME = getenv("RAILWAY_SERVICE_NAME")

# ==========================================
# 👑 MULTI OWNER SYSTEM
# ==========================================
OWNER_IDS = [8441236350, 6670240589, 8210605604, 5559682154, 1106006604]

# Main owner
OWNER_ID = OWNER_IDS[0]

# ==========================================
# 🛡️ SUDO USERS SYSTEM
# ==========================================
raw_sudo = getenv("SUDO_USERS", "8225211569,8707693929")
parsed_sudo = raw_sudo.replace(",", " ").split()
ENV_SUDO_IDS = []
SUDO_USERS = []
for user_id in parsed_sudo:
    try:
        uid = int(user_id)
        ENV_SUDO_IDS.append(uid)
        SUDO_USERS.append(uid)
    except ValueError:
        continue

# Add ALTRON users
for x in ALTRON:
    if x not in SUDO_USERS:
        SUDO_USERS.append(x)

# Add owners to sudo
for owner in OWNER_IDS:
    if owner not in SUDO_USERS:
        SUDO_USERS.append(owner)

# Remove duplicates
SUDO_USERS = list(set(SUDO_USERS))

# ==========================================
# 🤖 BOT TOKENS (AS YOU PROVIDED)
# ==========================================
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_TOKEN2 = getenv("BOT_TOKEN2", "")
BOT_TOKEN3 = getenv("BOT_TOKEN3", "")
BOT_TOKEN4 = getenv("BOT_TOKEN4", "")
BOT_TOKEN5 = getenv("BOT_TOKEN5", "")
BOT_TOKEN6 = getenv("BOT_TOKEN6", "")
BOT_TOKEN7 = getenv("BOT_TOKEN7", "")
BOT_TOKEN8 = getenv("BOT_TOKEN8", "")
BOT_TOKEN9 = getenv("BOT_TOKEN9", "")
BOT_TOKEN10 = getenv("BOT_TOKEN10", "")

# ==========================================
# 🤖 CLIENTS
# ==========================================
X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
