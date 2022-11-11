import requests
import telegram
import time
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from igromania import get_igromania_post
from coopland import get_coopland_post



load_dotenv()
token = os.getenv("TOKEN")
tg_chat_id = os.getenv("TG_CHAT_iD")
bot = telegram.Bot(token = "5490205792:AAFPDx8e6uNOdS8Dzp5e882B1hh1SpvkKZ4") 

with open("last_post_coopland.txt", "r", encoding="UTF-8") as my_file:
  last_post_coopland = my_file.read()
  
with open("last_post_igromania.txt", "r", encoding="UTF-8") as my_file:
    last_post_igromania = my_file.read()
    





while True:

    post_coopland=get_coopland_post()
    post_igromania=get_igromania_post()



    if post_coopland != last_post_coopland:
        with open (f'post_picture_coopland.jpg', "rb") as file:
            bot.send_photo(tg_chat_id,caption = post_coopland,photo =  file)
        last_post_coopland = post_coopland
        #print(last_post_coopland)
        with open("last_post_coopland.txt", "w", encoding="UTF-8") as my_file:
             my_file.write(post_coopland)
    

    if post_igromania != last_post_igromania:
        with open (f'post_picture_igromania.jpg', "rb") as file:
            bot.send_photo(tg_chat_id,caption = post_igromania,photo =  file)
        last_post_igromania = post_igromania
        #print(last_post_igromania)
        with open("last_post_igromania.txt", "w", encoding="UTF-8") as my_file:
                my_file.write(post_igromania)
        time.sleep(100)
