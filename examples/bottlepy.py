from bottle import route, run, template


@route('/name=<name>')
def index(name):
    print(name)
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)