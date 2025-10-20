# pretty printer

from urllib import request
import json

response = request.urlopen('https://jsonplaceholder.typicode.com/users')
response_json = response.read()
d = json.loads(response_json)

print(d)

print()
print()

from pprint import pprint
pprint(d)

print()
print()

pprint(d, depth=4, indent=1, width=200)