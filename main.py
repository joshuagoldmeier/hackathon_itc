from bottle import route, run, template
from Sports_Equipment import ski


# @route('/hello/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)
#
# run(host='localhost', port=8080)

for item in ski["Beginner"]:
    print("ski ", item)