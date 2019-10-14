import requests
from bs4 import BeautifulSoup
import xml


def top_news():
    url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, features="xml")

    items = soup.findAll('item')

    news_items = []

    for item in items:
        news_item = {}
        if item.title.text != '':
            news_item['title'] = item.title.text
            news_item['description'] = item.description.text
            news_item['link'] = item.link.text
            news_item['image'] = item.content['url']
            news_item['date'] = item.pubDate.text
            # news_item['date'] = datetime.strptime(item.pubDate.text,'%I, %d %M %Y %G:%i:%s %e' )

            news_items.append(news_item)
    return news_items

def international_news():
    url = "https://www.hindustantimes.com/rss/world/rssfeed.xml"

    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, features="xml")

    items = soup.findAll('item')

    news_items = []

    for item in items:
        news_item = {}
        if item.title.text != '':
            news_item['title'] = item.title.text
            news_item['description'] = item.description.text
            news_item['link'] = item.link.text
            news_item['image'] = item.content['url']
            news_item['date'] = item.pubDate.text
            news_items.append(news_item)
    return news_items

def national_news():
    url = "https://www.hindustantimes.com/rss/india/rssfeed.xml"

    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, features="xml")

    items = soup.findAll('item')

    news_items = []

    for item in items:
        news_item = {}
        if item.title.text != '':
            news_item['title'] = item.title.text
            news_item['description'] = item.description.text
            news_item['link'] = item.link.text
            news_item['image'] = item.content['url']
            news_item['date'] = item.pubDate.text
            news_items.append(news_item)
    return news_items

def headlines_news():
    url = "http://feeds.feedburner.com/ndtvnews-latest"

    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, features="xml")

    items = soup.findAll('item')

    news = []

    for item in items:
        new = {}
        print(item)
        if item.title.text != '':
            new['title'] = item.title.text
            new['link'] = item.link.text
            new['date'] = item.updatedAt.text
            news.append(new)
    return news