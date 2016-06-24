import json
from pprint import pprint

with open('sample.json') as data_file:
    data = json.load(data_file)

pprint(data)

print("---")

print(data["maps"][0]["id"])
print(data["masks"]["id"])
