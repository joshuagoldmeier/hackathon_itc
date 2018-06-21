from Sports_Equipment import sports
import json, urllib.request, sys, traceback, string
from pymongo import MongoClient


def process_description(item, description, answers):
    f = 0






def processItem(item, answers):
    best_item = []
    if "shortDescription" in item:
        description = item["shortDescription"].translate(str.maketrans("", "", string.punctuation)).lower()
        if answers[5] == item["gender"].lower():
            process_description(item, description, answers)












try:
    sports_dict = {}
    for sport_name, equipment in sports.items():
        cheapest_items = {}
        cheapest_item = {}
        main_dict = {}
        for item in equipment["Beginner"]:
            main_list = []
            final_json = {}
            x = 1
            while x < 26:
                keyWord = item.lower().replace("_", "%20")
                walmart_api = 'http://api.walmartlabs.com/v1/search?apiKey=utuc2y44uxauxzqk985vft4z&query="' + \
                              keyWord + '"&responseGroup=full&numItems=25&start=' + str(x)
                req = urllib.request.Request(walmart_api)
                final_req = urllib.request.urlopen(req).read()
                final_json = json.loads(final_req.decode('utf-8'))
                if "items" in final_json:
                    main_list += final_json["items"]
                x += 25
            final_json["items"] = main_list
            final_json["numItems"] = len(main_list)
            final_json.pop('start', None)
            main_dict[item.lower()] = final_json
            print(item.lower())


        print(json.dumps(main_dict))

        all_items = {}
        for key, value in main_dict.items():
            if len(value['items']) > 0:
                print(key)
                items_per_equipment = []
                for each_item in value['items']:
                    try:
                        item = {"Name": each_item['name'], "Price": each_item['salePrice'],
                                "URL": each_item['productUrl'], "Description": each_item['shortDescription'],
                                "Image": each_item['mediumImage'], "Size": each_item["size"]}
                        if "customerRating" in each_item:
                            item["CustomerRating"] = each_item["customerRating"]
                        if "gender" in each_item:
                            item["Gender"] = each_item["gender"]
                        items_per_equipment.append(item)
                    except Exception as e2:
                        traceback.print_exc()
                all_items[key] = items_per_equipment
        sports_dict[sport_name] = all_items


    #     for key, value in main_dict.items():
    #         if 'items' in value:
    #             cheapest_price = value['items'][0]['salePrice']
    #             cheapest_item = {"Name": value['items'][0]['name'], "Price": value['items'][0]['salePrice'],
    #                              "URL": value['items'][0]['productUrl'], "Description": value['items'][0]['longDescription'],
    #                              "Image": value['items'][0]['mediumImage']}
    #             for each_item in value['items']:
    #                 if each_item['salePrice'] < cheapest_price:
    #                     cheapest_price = each_item['salePrice']
    #                     cheapest_item = {"Name": each_item['name'], "Price": each_item['salePrice'],
    #                                      "URL": each_item['productUrl'], "Description": each_item['longDescription'],
    #                                      "Image": each_item['mediumImage']}
    #             cheapest_items[key] = cheapest_item
    #
    #     sports_dict[sport_name] = cheapest_items
    #     print("cheapest stuff:\n" + json.dumps(cheapest_items))
    #
    # print("final results\n" + json.dumps(sports_dict))
    #print (sports_dict)
    print(json.dumps(sports_dict))
    client = MongoClient('localhost', 27017)
    db = client.hackathon

    for key, value in sports_dict.items():
        db.items.update({"_id": key}, {"items": value}, upsert=True)

except Exception as e:
    traceback.print_exc()