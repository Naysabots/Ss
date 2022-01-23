import pyrogram
import os
from pyrogram import filters
from pyrogram.types import Message, User
from pyrogram import Client as NaysaBots



       
       
   
  
@NaysaBots.on_message(filters.forwarded & filters.channel)
async def restricted(bot, message):
    
