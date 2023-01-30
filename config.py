import os

from pyrogram import Client

API_ID = int(os.environ.get("API_ID", "10683462"))
API_HASH = os.environ.get("API_HASH", "8ab812d6e6849bd6352dcb731e44c31e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5680348811:AAFTg0TmzNx6dBPG5A2TQ3meJq3_npGVs2A")
# it's for start/help texts. It will NO for url/playlist uploader
BITLY_KEY = [
    "ece4c420f32b4f977b9b68bee620ef4c16fb79c2",
    "711fd58f7c83834528956257cac3294d98a4a738",
    "79faedc136c03de6202480e3476b37e195347360",
    "f5981ade3b0e3cf080077c4424fff57ceb950a5a",]
SEND_TEXT = """ Hello {},
I am Bitly Bot to shorten links.
Send a valid link to shorten.

Deployed with ❤️ By @DKBOTZ
"""

bot = Client(
    name="mybot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)
