from django.shortcuts import render
from newsapi import NewsApiClient
import json
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
def home(request):
    news = NewsApiClient(api_key = '4df4877345ba4b0086fe1570c1e486a1')
    all_climate_headlines = news.get_everything(q='climate change')
    climate_headlines_cnn = news.get_everything(q='climate change',sources = 'CNN')
    climate_headlines_bbc = news.get_everything(q='climate change',sources = 'BBC-News')
    climate_headlines_i = news.get_everything(q='climate change',sources = 'independent')
    climate_headlines_fn = news.get_everything(q='climate change',sources = 'fox-news')
    climate_headlines_toi = news.get_everything(q='climate change',sources = 'the-times-of-india')
    # return JsonResponse(all_climate_headlines['articles'],safe=False)

    articles = {
        'articles_cnn':climate_headlines_cnn['articles'][:4],
        'articles_bbc':climate_headlines_bbc['articles'][:4],
        'articles_i':climate_headlines_i['articles'][:4],
        'articles_fn':climate_headlines_fn['articles'][:4],
        'articles_toi':climate_headlines_toi['articles'][:4],
    }
    allsources = [

        {'name':'CNN','id':'cnn'},
        {'name':'BBC News','id':'bbc-news'},
        {'name':'Fox News','id':'fox-news'},
        {'name':'Independent','id':'independent'},
        {'name':'The Times Of India','id':'the-times-of-india'

        }]

    return render(request,'news/news1.01.html',{'all_articles':articles,'allsources':allsources})

def eachsource(request,source):
    news = NewsApiClient(api_key = '4df4877345ba4b0086fe1570c1e486a1')
    each_climate_headlines = news.get_everything(q='climate change',sources=source)
    # return JsonResponse(each_climate_headlines['articles'],safe=False)

    allsources = [

        {'name':'CNN','id':'cnn'},
        {'name':'BBC News','id':'bbc-news'},
        {'name':'Fox News','id':'fox-news'},
        {'name':'Independent','id':'independent'},
        {'name':'The Times Of India','id':'the-times-of-india'}
        
        ]
    return render(request,'news/news_each.html',{'articles':each_climate_headlines['articles'],'allsources':allsources})