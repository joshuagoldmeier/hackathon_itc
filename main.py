from bottle import route,static_file, run, template, get,request
import json
import bottle as b
from pymongo import MongoClient


info_list=[]
question_list=["Which sport would you like to take a wack at?","what is your level in this sport",
               "What is your height?(cm please)","what is your weight(kg please)?",
               "last question,what is your budget(only numbers in dollars)"]

@get("/")
def index():
    return template("landing.html")


@get("/boto")
def index():
    return template("boto.html")


@get("/mainpage")
def index():
    return template("mainpage.html")


@route("/chat", method='POST')
def chat():
    if len(info_list)==0:
        name = request.POST.get('msg')
        info_list.append(name)

        return json.dumps({"animation": "speaking", "msg": question_list[0],"status":False})

    if len(info_list)== 1:
        sport = request.POST.get('msg')
        info_list.append(sport)

        return json.dumps({"animation": "speaking", "msg": question_list[1],"status":False})

    if len(info_list) == 2:
        level = request.POST.get('msg')
        info_list.append(level)

        return json.dumps({"animation": "speaking", "msg": question_list[2],"status":False})

    if len(info_list) == 3:
        height = request.POST.get('msg')
        info_list.append(height)

        return json.dumps({"animation": "speaking", "msg": question_list[3],"status":False})

    if len(info_list) == 4:
        weight = request.POST.get('msg')
        info_list.append(weight)

        return json.dumps({"animation": "speaking", "msg": question_list[4],"status":False})

    if len(info_list) == 5:
        budget = request.POST.get('msg')
        info_list.append(budget)
        print (info_list)

        return json.dumps({"animation": "speaking",
                           "msg": "ok thank you we will find all the products you need !!","status":True})



@get("/sports/ski")
def sports():
    return json.dumps(info_list)


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)



@get("/")
def index():
    return template("index.html")


@get("/sports/ski")
def sports():
    print("In the route")
    items_to_return = {}
    equipment_keywords = ["soccer_ball", "volleyball", "football", "basketball", "hockey_puck", "baseball",]
    age = int(info_list[5])
    height = int(info_list[3])
    weight = int(info_list[4])
    budget = int(info_list[7])

    gender = "male" if info_list[6] == "man" else "female"
    male_keywords = ['boy', 'kid', 'youth'] if age < 18 else ['men', 'adult']
    female_keywords = ['girl', 'kid', 'youth'] if age < 18 else ['women', 'adult']
    client = MongoClient('localhost', 27017)
    db = client.hackathon
    all_sports = db.items.find()
    for sport in all_sports:
        if sport["_id"].lower() == info_list[1].lower():
            for equipment_name, equipment_list in sport["items"].items():
                print(equipment_name)
                for one_equip in equipment_list:
                    if equipment_name not in equipment_keywords:
                        if "Gender" in one_equip:
                            if one_equip["Gender"].lower() == gender:
                                if 'female' in gender:
                                    for kw in female_keywords:
                                        if kw.lower() in one_equip['Name'].lower():
                                            items_to_return[equipment_name] = one_equip
                                else:
                                    for kw in male_keywords:
                                        if kw.lower() in one_equip['Name'].lower():
                                            items_to_return[equipment_name] = one_equip
                            elif one_equip["Gender"] == "Unisex":
                                if height > 150 and weight > 70:
                                    if "medium" in one_equip["Size"].lower() or "medium" in one_equip["Description"].lower():
                                        items_to_return[equipment_name] = one_equip
                                    elif "large" in one_equip["Size"].lower() or "large" in one_equip["Description"].lower():
                                        items_to_return[equipment_name] = one_equip
                                else:
                                    if "medium" in one_equip["Size"].lower() or "medium" in one_equip["Description"].lower():
                                        items_to_return[equipment_name] = one_equip
                                    elif "small" in one_equip["Size"].lower() or "small" in one_equip["Description"].lower():
                                        items_to_return[equipment_name] = one_equip
                        else:
                            if height > 150 and weight > 70:
                                if "medium" in one_equip["Size"].lower() or "medium" in one_equip["Description"].lower():
                                    items_to_return[equipment_name] = one_equip
                                elif "large" in one_equip["Size"].lower() or "large" in one_equip["Description"].lower():
                                    items_to_return[equipment_name] = one_equip
                            else:
                                if "medium" in one_equip["Size"].lower() or "medium" in one_equip["Description"].lower():
                                    items_to_return[equipment_name] = one_equip
                                elif "small" in one_equip["Size"].lower() or "small" in one_equip["Description"].lower():
                                    items_to_return[equipment_name] = one_equip
                    else:
                        if "size 5" in one_equip['Name'].lower() or "official size" in one_equip['Description'].lower():
                                    items_to_return[equipment_name] = one_equip




    print (items_to_return)
    return json.dumps(items_to_return) if len(items_to_return) > 0 else "Sorry, we cannot find you a match :("


# @get("/sport/<sport_name>")
# def index(sport_name):
#     client = MongoClient('localhost', 27017)
#     db = client.hackathon
#     items = db.items.find()
#     print(items)
#     for item in items:
#         if item["_id"] == sport_name:
#             return item
#     return "can't find sport!"

@get("/sport/<sport_name>")
def index(sport_name):
    client = MongoClient('localhost', 27017)
    db = client.hackathon
    items = db.items.find()
    print(items)
    for item in items:
        if item["_id"] == sport_name:
            return item
    return "can't find sport!"

@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return b.static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def css(filename):
    return b.static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()
