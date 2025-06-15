import requests

api = 'dea9b9a7b67a4542bc8671fef6e5fcbe'
url = ('https://newsapi.org/v2/everything?q=tesla'
       '&from=2025-05-15&sortBy=publishedAt&'
       'apiKey=dea9b9a7b67a4542bc8671fef6e5fcbe')

request = requests.get(url)
content = request.json()

for article in content['articles']:
       print(article['title'])
       print(article['description'])