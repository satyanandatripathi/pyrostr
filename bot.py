import os

from heroku3 import from_key
from pyrogram import Client
from pyromod import listen

API_ID =3964003 #int(os.environ.get("API_ID", 0))
API_HASH =4f88fd6f20f778245182202e2dd34ee0 #os.environ.get("API_HASH", None)
BOT_TOKEN =1825593454:AAFonNM8mTaCY5Vu42KJX-zEwIPj_wAD7wA #os.environ.get("BOT_TOKEN", None)
APP_NAME = os.environ.get("APP_NAME", None)
API_KEY = os.environ.get("API_KEY", None)
HU_APP = from_key(API_KEY).apps()[APP_NAME]

bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
