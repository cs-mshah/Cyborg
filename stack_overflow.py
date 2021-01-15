import requests
from requests.exceptions import HTTPError
 
# https://api.stackexchange.com/docs/advanced-search
 
query = "how to start programming in Python"
tags = ("python", "beginner")
params = {'q': query, 'tagged': tags, 'sort': 'relevance', 'page': '1', 'pagesize': '5', 'order': 'desc', 'site': 'stackoverflow'}
 
try:
    response = requests.get('https://api.stackexchange.com/2.2/search/advanced/', params=params)
 
    js = response.json()
    
    for item in js['items']:
        print(item['title'])
 
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
 
except Exception as err:
    print(f'Other error occurred: {err}')