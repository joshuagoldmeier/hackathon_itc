from Sports_Equipment import ski
from bottle import route,static_file, run, template, get,request
import json
import bottle as b


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
    user_message = request.POST.get('msg')

    return json.dumps({"animation": "speaking", "msg": user_message})


@get("/sports/ski")
def sports():
    my_list = ["gloves","hellmet","glasses","boots"]
    return json.dumps(my_list)


keyWord = ""
walmart_api = 'http://api.walmartlabs.com/v1/search?apiKey=utuc2y44uxauxzqk985vft4z&query="' + keyWord + '"'


# @route('/hello/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)
#
# run(host='localhost', port=8080)

for item in ski["Beginner"]:
    print("ski ", item)


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
