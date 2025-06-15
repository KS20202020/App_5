import requests
from send_email import send_email

api = 'dea9b9a7b67a4542bc8671fef6e5fcbe'
url = ('https://newsapi.org/v2/everything?q=tesla'
       '&from=2025-05-15&sortBy=publishedAt&'
       'apiKey=dea9b9a7b67a4542bc8671fef6e5fcbe')

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article's title & description
body = ''
for article in content['articles']:
       title = article['title']
       description = article['description']
       if article['title'] is not None:
              body = body + article['title'] + '\n' + article['description'] + 2*'\n'

body = body.encode('utf-8')
send_email(message=body)

