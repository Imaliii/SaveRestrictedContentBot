#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "19885933"
API_HASH = "6ced806df9b7ef110a95464b7768f098"
BOT_TOKEN = "5996995992:AAHfz17sXwoG4QActpdX1lMipXcOc5H9aIs"
SESSION = "1BJWap1wBuxfs1Wxue21CjQTsDRPDlVbbjDoV6okY-_7XxYLTdbnu8_mah1_KqDaQrg2poNSWwTWb6cm5CCiJzAj9NgIaKqGWc_asRwwfq7DFLgoH9ZUN7Ql0C90Hrf1aePOmKoRuEIJ5QW_kjlHKBUp9jbgwDzQPqbSIuMD5ZqcQjSFbP2iAbRPHxeg719HZ4jUKCAryaND4PbPuHJGprswkS1sqfHozVvu8dcXf4fZQiFXTxOtfaD5eLs2d567xmHRFVpFZzomtncswJ8lZ6uwC1F67NpWtIvCZt-ws5IL2yL9faObuieGMPNrRS2-QyGWCGg_qzUtn6WGvh10S7-PhL0aKyyg="
FORCESUB = config("FORCESUB", default=None)
AUTH = "734352872"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
