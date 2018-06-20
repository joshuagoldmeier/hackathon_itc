from bottle import route, run, template, get
import bottle as b
from pymongo import MongoClient
import json



@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)



@get("/")
def index():
    return template("index.html")

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


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
