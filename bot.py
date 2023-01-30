from config import bot, SEND_TEXT
import re
from BitlyAPI import shorten_urls
from BitlyAPI.exceptions import BitlyException, BitlyApiNotWorking

from pyrogram import filters
from pyrogram.types import Message


# Replace Link
async def replace_link(dkbotz):
    links = await extract_link(dkbotz)

    for link in links:
        long_url = link
        prin(long_url)
        should_replace_link = True

        if should_replace_link:
            dkbotz = await shorten_urls(dkbotz)
            print (dkbotz)
            text = text.replace(long_url, dkbotz)
            print(text)
    return text

## Link 
async def extract_link(string):
	"""
	It takes a string and returns a list of all the URLs in that string
	
	:param string: The string to search for links in
	:return: A list of urls
	"""
	urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
	return urls

@bot.on_message(filters.private & filters.command("start"))
async def start_(_, msg: Message):
    await msg.reply(
        SEND_TEXT.format(msg.from_user.mention),
        disable_web_page_preview=True
    )

##### Channel Convert By @DKBOTZ #### DON'T REMOVE CREDIT 💳

@bot.on_message(filters.channel & filters.incoming)
async def by_dkbotz(_, message: Message):
    dkbotz = message.caption or message.text
    dk_id = message.chat.id
    print(f'Message Recived From {dk_id}')

    dkbotz = await replace_link(dkbotz)
    print ('Short Completed')
    await message.edit(dkbotz)
    return 





if __name__ == "__main__":
    bot.run()
