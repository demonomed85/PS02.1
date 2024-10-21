import requests
import pprint

q = 'html'
response = requests.get('https://api.github.com/events', params={'q':q})
print(response.status_code)

response_json = response.json()
pprint.pprint(response_json)