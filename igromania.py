import requests
import telegram
import time
from bs4 import BeautifulSoup


def get_igromania_post():
        #-----------------igromania-----------------
    url_igromania = f'https://www.igromania.ru/news/'
    response_igromania = requests.get(url_igromania)
    soup_igromania = BeautifulSoup(response_igromania.text, features="html.parser")
    aubli_data = soup_igromania.find('div',class_="aubli_data")
    headers_igromania = aubli_data.find('a',class_ = "aubli_name").text
    description_igromania = aubli_data.find('div', class_ ="aubli_desc").text
    incomplete_link_article_igromania = aubli_data.find('a', class_ = "aubli_name")["href"]
    aubl_item = soup_igromania.find('div', class_ = "aubl_item")
    picture_url_igromania = aubl_item.find('img')["src"]
    complete_url_article_igromania = f"https://www.igromania.ru{incomplete_link_article_igromania}"

    post_picture_igromania = requests.get(picture_url_igromania)
    with open("post_picture_igromania.jpg", "wb") as file:
        file.write(post_picture_igromania.content)

    post_igromania = (f"""{headers_igromania}

{description_igromania}

Ссылка на источник: {complete_url_article_igromania}

    """)
    return post_igromania
