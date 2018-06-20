from Sports_Equipment import ski
from bottle import route, run, template, get
import bottle as b


@get("/")
def index():
    return template("landing.html")

@get("/mainpage")
def index():
    return template("mainpage.html")

@get("/sports/ski")
def sports():
    my_list = ["ski"]
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


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
