from django.shortcuts import render
from newsapi import NewsApiClient
import json
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
def home(request):
    news = NewsApiClient(api_key = '1a04cf5f282d49f18febc30f7cd22ddc')
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

    return render(request,'news/news.html',{'articles':articles})

def eachsource(request,source):
    news = NewsApiClient(api_key = '1a04cf5f282d49f18febc30f7cd22ddc')
    each_climate_headlines = news.get_everything(q='climate change',sources=source)
    # return JsonResponse(each_climate_headlines['articles'],safe=False)
    return render(request,'news/news_each.html',{'articles':each_climate_headlines['articles']})