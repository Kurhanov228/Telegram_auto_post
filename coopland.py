import requests
import telegram
import time
from bs4 import BeautifulSoup


def get_coopland_post():    #-----------------COOPLAND-----------------
    url_coopland = f'https://coop-land.ru/helpguides/new/'
    response_coopland = requests.get(url_coopland)
    soup_coopland = BeautifulSoup(response_coopland.text, features="html.parser")
    artical_content = soup_coopland.find('div',class_="article-content")
    headers_coopland = artical_content.find('h2',class_="title").text
    description_coopland = artical_content.find('div',class_="preview-text").text

    article_clr_coopland = soup_coopland.find('div', class_="article clr")
    url_article = soup_coopland.find('a', class_="big-link")["href"]

    photo_content = soup_coopland.find('article',class_="news")
    photo = photo_content.find('img')["data-src"]
    picture_url_coopland = (f'https://coop-land.ru/{photo}')

    post_picture_coopland = requests.get(picture_url_coopland)
    with open("post_picture_coopland.jpg", "wb") as file:
        file.write(post_picture_coopland.content)

    post_coopland = (f"""{headers_coopland}

{description_coopland}

Ссылка на источник: {url_article}

    """)
    return post_coopland
