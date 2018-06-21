from bottle import route,static_file, run, template, get,request,response
import json
import bottle as b
from Sports_Equipment import sports
from pymongo import MongoClient


info_list=[]

question_list=["ok {} , nice to meet you !Which sport would you like to take a whack at?","what is your level in this sport (beginner,amateur,professional)",
               "What is your height?(cm please)","what is your weight(kg please)?","What is your age ?",
               "Are you a man or a woman?(I know its's a lot of questions but we really want to help you!)",
               "last question,what is your budget(only numbers in dollars)"]

error_answer ="If you want GEAROBOT to help you please give us a correct answer,maybe you didn't type it right :)"


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
    if len(info_list) == 0:
        user_message = request.POST.get('msg')
        while not get_user_name(user_message):
            return json.dumps({"animation": "speaking", "msg": error_answer, "status": 0})

        name = get_user_name(user_message)

        response.set_cookie('name', name)

        info_list.append(name)
        return json.dumps({"animation": "speaking", "msg": question_list[0].format(name),"status":0})

    if len(info_list)== 1:
        user_message = request.POST.get('msg')
        while not get_user_sport(user_message):
            return json.dumps(
                {"animation]": "speaking", "msg":error_answer,"status" : 0})

        sport = get_user_sport(user_message)
        info_list.append(sport)
        return json.dumps({"animation": "speaking", "msg": question_list[1],"status":0})

    if len(info_list) == 2:
        user_message = request.POST.get('msg')
        while not get_user_level(user_message):
            return json.dumps(
                {"animation]": "speaking", "msg": error_answer, "status": 0})

        level = get_user_level(user_message)
        info_list.append(level)

        return json.dumps({"animation": "speaking", "msg": question_list[2],"status":0})

    if len(info_list) == 3:
        height = request.POST.get('msg')
        while not height.isdigit():
            return json.dumps({"animation": "speaking", "msg": error_answer, "status": 0})

        info_list.append(height)

        return json.dumps({"animation": "speaking", "msg": question_list[3],"status":0})

    if len(info_list) == 4:
        weight = request.POST.get('msg')
        while not weight.isdigit():
            return json.dumps({"animation": "speaking", "msg": error_answer, "status": 0})

        info_list.append(weight)

        return json.dumps({"animation": "speaking", "msg": question_list[4],"status":0})

    if len(info_list) == 5:
        age = request.POST.get('msg')
        while not age.isdigit():
            return json.dumps({"animation": "speaking", "msg": error_answer, "status": 0})

        info_list.append(age)

        return json.dumps({"animation": "speaking", "msg": question_list[5],"status":0})


    if len(info_list) == 6:
        user_message = request.POST.get('msg')
        while not get_user_gender(user_message):
            return json.dumps({"animation": "speaking", "msg": error_answer, "status": 0})

        gender = get_user_gender(user_message)
        info_list.append(gender)

        return json.dumps({"animation": "speaking", "msg": question_list[6],"status":0})

    if len(info_list) == 7:
        budget = request.POST.get('msg')
        while not budget.isdigit():
            return json.dumps({"animation": "speaking", "msg": error_answer, "status": 0})

        info_list.append(budget)

        return json.dumps({"animation": "zidane",
                           "msg": "ok thank you we will find all the products you need !!","status":1})


def get_user_name(user_message):

    user_message =user_message.lower()
    user_message_splited = user_message.split()
    name_list = ["boto", "my", "am", "i", "hello", "name", "is"]
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for word in user_message_splited:
        if word in name_list or word.isdigit() or word in punctuations:
            continue
        else:
            return word
    return False


def get_user_sport(user_message):

    user_message = user_message.lower()
    user_message_splited = user_message.split()
    sport_list = ["ski","soccer","basketball","danse"]
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for word in user_message_splited:
        if word not in sport_list or word.isdigit() or word in punctuations:
            continue
        else:
            return word
    return False


def get_user_level(user_message):
    user_message = user_message.lower()
    user_message_splited = user_message.split()

    level_list = ["beginner","amateur","professional"]
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for word in user_message_splited:
        if word not in level_list or word.isdigit() or word in punctuations:
            continue
        else:
            return word
    return False


def get_user_gender(user_message):
    user_message = user_message.lower()
    user_message_splited = user_message.split()

    gender_list = ["man","woman"]
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for word in user_message_splited:
        if word not in gender_list or word.isdigit() or word in punctuations:
            continue
        else:
            return word
    return False

@get("/sports/ski")
def sports():
    print("In the route")
    items_to_return = {}
    age = int(info_list[5])
    height = info_list[3]
    weight = info_list[4]
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
                    if "Gender" in one_equip:
                        if one_equip["Gender"].lower() == gender:
                            if 'male' in gender:
                                for kw in male_keywords:
                                    if kw.lower() in one_equip['Name'].lower():
                                        items_to_return[equipment_name] = one_equip
                            else:
                                for kw in female_keywords:
                                    if kw.lower() in one_equip['Name'].lower():
                                        items_to_return[equipment_name] = one_equip
                        elif one_equip["Gender"] == "Unisex":
                            print(8)
    print (items_to_return)
    return json.dumps(items_to_return) if len(items_to_return) > 0 else "Sorry, we cannot find you a match :("


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
