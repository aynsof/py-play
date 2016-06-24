import json, yaml
from pprint import pprint

with open('sample.json') as data_file:
    data = json.load(data_file)

yml = yaml.safe_dump(data)

f = open('out.yaml', 'w')
f.write(yml)
f.close()

pprint(data)

print("---")

print(data["maps"][0]["id"])
print(data["masks"]["id"])
