import os

from heroku3 import from_key
from pyrogram import Client
from pyromod import listen

API_ID=os.environ.get("API_ID", None)
API_HASH=os.environ.get("API_HASH", None)
BOT_TOKEN=os.environ.get("BOT_TOKEN", None)


bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
