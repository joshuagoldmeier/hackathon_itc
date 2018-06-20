from bottle import route, run, template


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)


keyWord = ""
walmart_api = 'http://api.walmartlabs.com/v1/search?apiKey=utuc2y44uxauxzqk985vft4z&query="' + keyWord + '"'
