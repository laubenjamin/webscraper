import webscraper
import json

with open('twitterData.json') as json_data:
    jsonData = json.load(json_data)
for i in jsonData:
    like = 0
    for x in range(len(i['likes'])):
        if i["likes"][x].isdigit():
            like = x
            break
    if 100 < int(i['likes'][like:]):
        print (i['tweet'])
        print (i["likes"])