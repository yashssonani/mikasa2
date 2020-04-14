
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
"""
USER_NAME = "hello"
PASSWORD = "MOJO"
new_download_locatio ="king"
url = "king"
sent_message_to_update_tg_p = "king"
c_file_name = "king"
"""
async def plu_dl(url,sent_message_to_update_tg_p,c_file_name):
    eco = command_exec(url,c_file_name)
    to_upload_file = c_file_name
    response = {}
    LOGGER.info(response)
    user_id = sent_message_to_update_tg_p.reply_to_message.from_user.id
    final_response = await upload_to_tg(
        sent_message_to_update_tg_p,
        to_upload_file,
        user_id,
        response
    )
    return_name = eco
    return return_name   




async def command_exec(url,new_download_location): 
    command =[
         "youtube-dl",
         "u"+USER_NAME,
         "p"+PASSWORD,
         "--no-warnings",
         "--console-title",
         "--max-sleep-interval20",
         "--min-sleep-interval15",
         "-o"+new_download_location+"%(playlist_title)s/%(chapter_number)s - %(chapter)s/%(playlist_index)s-%(title)s.%(ext)s",
         url
    ]   
    process = call(command, shell=False)
    return_name = new_download_location
    return return_name
