from newsapi import NewsApiClient

def run():
    newsapi = NewsApiClient(api_key='1a04cf5f282d49f18febc30f7cd22ddc')
    top_headlines = newsapi.get_top_headlines(q='climate',language='en',country='us')
    print(top_headlines)