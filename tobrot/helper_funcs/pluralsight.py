
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import asyncio
import os
import time
import subprocess
from tobrot.helper_funcs.upload_to_tg import upload_to_tg
from subprocess import call 

from tobrot import (
    DOWNLOAD_LOCATION,
    USER_NAME,
    PASSWORD
)

async def plu_dl(url, sent_message_to_update_tg_p):

    url = url
    # create an unique directory
    new_download_location = os.path.join(
        DOWNLOAD_LOCATION,
        str(current_user_id),
        str(time.time())
    )
    # create download directory, if not exist
    if not os.path.isdir(new_download_location):
        os.makedirs(new_download_location)
    #await i_m_sefg.edit_text("trying to download")

    #command = "youtube-dl -o /storage/emulated/0/Videoder/%(title)s.%(ext)s https://youtu.be/_eH356kyvvw -c" 
    command = "youtube-dl"
    command = command + " -u " + USER_NAME
    command = command + " -p " + PASSWORD
    command = command + " -i -c --no-warnings --console-title --max-sleep-interval 20 --min-sleep-interval 10"
    command = command + " --playlist-start 3 --playlist-end 4"
    command = command + " -o " + new_download_location + "%(playlist_title)s/%(chapter_number)s - %(chapter)s/%(playlist_index)s-%(title)s.%(ext)s "
    command = command + url
    #print(command)

    call(command.split(), shell=False)
    to_upload_file = new_download_location


    response = {}
    LOGGER.info(response)
    user_id = sent_message_to_update_tg_p.reply_to_message.from_user.id
    final_response = await upload_to_tg(
        sent_message_to_update_tg_p,
        to_upload_file,
        user_id,
        response
    )

     
        
             return_name = new_download_location
    return return_name





"""
command = "youtube-dl -o /storage/emulated/0/Videoder/%(title)s.%(ext)s https://youtu.be/_eH356kyvvw -c" 


USER_NAME = "hello"
PASSWORD = "yash"
new_download_location = "mojilo"
url = "kemcho"
"""



"""
"youtube-dl -u" USER_NAME "-p" PASSWORD" -i -c --no-warnings --playlist-start "10" --console-title --max-sleep-interval 20 --min-sleep-interval 10 -o '%(playlist_title)s/%(chapter_number)s - %(chapter)s/%(playlist_index)s-%(title)s.%(ext)s'+url
"""