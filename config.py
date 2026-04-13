import logging

from telethon import TelegramClient

from os import getenv
from RAUSHAN.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = "35411328"
API_HASH = "4c8d3c8f5d3483296f5fb530ea2cfcc6"
MONGO_URI = "mongodb+srv://rj5706603:O95nvJYxapyDHfkw@cluster0.fzmckei.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "cb2147ff-d743-49fc-a18e-6a40aec75e77")

BOT_TOKEN = getenv("8729582864:AAEsEADH7wQXOlV5hm8bT1f_LhmLoN_INB0", default=None)
BOT_TOKEN2 = getenv("8492531985:AAFfpR_e_hVglfNNi54xgCIFkr2fO50aNlk", default=None)
BOT_TOKEN3 = getenv("8611361143:AAEfCrWbD_JODP3DNB9yLMBVN74nR0WZfyM", default=None)
BOT_TOKEN4 = getenv("8749385192:AAHgpwpu6Hy9mIUa6k2fX4wQ6Qr38qLqW38", default=None)
BOT_TOKEN5 = getenv("7979190403:AAFEu10OyXfdRi4ckTWjpfnRjmpXuMKZcts", default=None)
BOT_TOKEN6 = getenv("8637265090:AAHDkPQ81u5ZBUtD-J2HHMoMoL53I-TZ_1I", default=None)
BOT_TOKEN7 = getenv("8740366034:AAFF7sjnHH_R7LcBWS7e42dSBG07o9PwNng", default=None)
BOT_TOKEN8 = getenv("8721234505:AAEA_BMNvqrWq07wTKxzoQ98LgEWEizn6-I", default=None)
BOT_TOKEN9 = getenv("8715356761:AAFZ7RYkmt0B483xp6rsYTaEnNvIKHtbRGU", default=None)
BOT_TOKEN10 = getenv("8514898003:AAFZyxjZOoI6lxIzzuV3glpvCLat8WknfNk", default=None)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="8441236350").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="8441236350"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

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

