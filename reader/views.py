from django.shortcuts import render
from .parser import top_news, international_news, national_news, headlines_news


def home(request):
    # call top_news function from parser file
    news_items = top_news()
    headlines = headlines_news()
    # send data to template
    return render(request,'home.html',{'feed':news_items, 'headlines':headlines})

def international(request):
    # call international_news function from parser file
    news_items = international_news()
    # send data to template
    return render(request,'international.html',{'feed':news_items})

def national(request):
    # call national_news function from parser file
    news_items = national_news()
    # send data to template
    return render(request,'national.html',{'feed':news_items})