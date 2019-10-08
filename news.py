from newsapi import NewsApiClient
from key import x_api_key 
import requests


url = 'https://newsapi.org/v2/top-headlines'
sources = ['cnn', 'bbc-news', 'fox-news']
headlines = {}
for source in sources:
    full_url = f"{url}?sources={source}"
    response = requests.get(full_url, headers={"x-api-key": x_api_key})
    headlines[source] = response.json()


cnn_headlines = headlines['cnn']['articles']

print('CNN')
for headline in cnn_headlines:
    print(headline['title'])
    
print()

bbc_headlines = headlines['bbc-news']['articles']

print('BBC')
for headline in bbc_headlines:
    print(headline['title'])

print()

fox_headlines = headlines['fox-news']['articles']

print('FOX')
for headline in fox_headlines:
    print(headline['title'])










