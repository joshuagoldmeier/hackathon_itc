from bottle import route,static_file, run, template, get,request
import json
import bottle as b

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
    items_to_return = {}
    age = info_list[5]
    height = info_list[3]
    weight = info_list[4]
    gender = info_list[6]
    keywords = ['boy', 'girl', 'kid', 'youth'] if age < 18 else ['men', 'women', 'adult']
    client = MongoClient('localhost', 27017)
    db = client.hackathon
    items = db.items.find()
    print(items)
    for item in items:
        if item["_id"].lower() == info_list[1].lower():
            for equipment_name, equipment_list in item.items():
                for one_equip in equipment_list:
                    if "Gender" in one_equip:
                        if one_equip["Gender"] == "Unisex" or one_equip["Gender"] == gender:
                            for kw in keywords:
                                if kw in one_equip['Name'].lower():
                                    items_to_return[equipment_name] = one_equip


    return json.dumps(items_to_return) if len(items_to_return) > 0 else "Sorry, we cannot find you a match :("

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


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
