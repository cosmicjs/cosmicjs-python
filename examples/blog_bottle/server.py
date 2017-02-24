from bottle import route, run, template
from pythoncosmicjs import Api

api = Api('pythoncosmicjs', write_key='9rIG8XYnKDP60MtIis8ORv1pzgp2kYsT7PsXyV1yciqwaNIpPC')


@route('/<name>')
def index(name):
    if name != 'favicon.ico':
        post = api.one_object(name)
        return template('post', name=name, title=post['object']['title'], content=post['object']['content'])
run(host='localhost', port=8080)