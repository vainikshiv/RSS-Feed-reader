from django.shortcuts import render
import feedparser
import requests
from bs4 import BeautifulSoup
import xml


# Create your views here.
def home(request):
    # d = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml')
    # for entry in d.entries:
    #     print(entry,'\n')
    # url = "http://feeds.bbci.co.uk/news/rss.xml"
    url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, features="xml")

    items = soup.findAll('item')

    news_items = []

    for item in items:
        print(item)
        news_item = {}
        if item.title.text != '':
            news_item['title'] = item.title.text
            news_item['description'] = item.description.text
            news_item['link'] = item.link.text
            news_item['image'] = item.content['url']
            news_item['date'] = item.pubDate.text
            news_items.append(news_item)

    # print(news_items)
    return render(request,'home.html',{'feed':news_items})