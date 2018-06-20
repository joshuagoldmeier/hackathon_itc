from bottle import route, run, template,get
import bottle as b

@get("/")
def index():
    return template("index.html")


@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return b.static_file(filename, root='js')


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()
run(host='localhost', port=8080)