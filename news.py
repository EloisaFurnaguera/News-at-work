from newsapi import NewsApiClient
import requests

# url = ('https://newsapi.org/v2/top-headlines?'
#        'country=us&'
#        'apiKey=3fe40963db1048039a461036e091f55b')

# response = requests.get(url)


# # print (response.json())
# #print(response.headers)
# for x in response.json():
#     print ([x][1])



    # articles

#for ony one news souece

# url = ('https://newsapi.org/v2/top-headlines?'
#        'sources=bbc-news&'
#        'apiKey=')
# response = requests.get(url)
# # print (response.json())

# mama = response.json()

# # print (response)

# for x in mama['articles']:
#     # print(x['title'])

#     print(x['author'], x['title'])





url = ('https://newsapi.org/v2/top-headlines?'
       'sources=cnn&'
       'apiKey=')

response = requests.get(url)
print (response.json())

mama = response.json()
print(mama)

# print (response)

# for x in mama['articles']:
#     # print(x['title'])

#     print(x['author'], x['title'])
