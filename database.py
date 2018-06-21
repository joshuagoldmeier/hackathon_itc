from Sports_Equipment import sports
import json, urllib.request, sys, traceback
from pymongo import MongoClient


try:
    sports_dict = {}
    for sport_name, equipment in sports.items():
        cheapest_items = {}
        cheapest_item = {}
        main_dict = {}

        for item in equipment["Beginner"]:
            keyWord = item.lower().replace("_", "%20")
            walmart_api = 'http://api.walmartlabs.com/v1/search?apiKey=utuc2y44uxauxzqk985vft4z&query="' + keyWord + '"'
            req = urllib.request.Request(walmart_api)
            final_req = urllib.request.urlopen(req).read()
            final_json = json.loads(final_req.decode('utf-8'))
            main_dict[item.lower()] = final_json
            print(item.lower())

        for key, value in main_dict.items():
            if 'items' in value:
                cheapest_price = value['items'][0]['salePrice']
                cheapest_item = {"Name": value['items'][0]['name'], "Price": value['items'][0]['salePrice'],
                                 "URL": value['items'][0]['productUrl'], "Description": value['items'][0]['longDescription'],
                                 "Image": value['items'][0]['mediumImage']}
                for each_item in value['items']:
                    if each_item['salePrice'] < cheapest_price:
                        cheapest_price = each_item['salePrice']
                        cheapest_item = {"Name": each_item['name'], "Price": each_item['salePrice'],
                                         "URL": each_item['productUrl'], "Description": each_item['longDescription'],
                                         "Image": each_item['mediumImage']}
                cheapest_items[key] = cheapest_item

        sports_dict[sport_name] = cheapest_items

    j = json.dumps(sports_dict)
    print(j)

    client = MongoClient('localhost', 27017)
    db = client.hackathon

    for key, value in sports_dict.items():
        db.items.update({"_id": key}, {"items": value}, upsert=True)

except Exception as e:
    traceback.print_exc()