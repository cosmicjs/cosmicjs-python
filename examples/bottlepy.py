from bottle import route, run, template
from pythoncosmicjs import Api
api = Api('pythoncosmicjs')


@route('/')
def index():
    post_list = api.list_objects()
    return template('<a href="{{url}}">{{title}}</a>', title=post_list['objects'][0]['title'], url=post_list['objects'][0]['slug'])


@route('/<blog_name>')
def blog(blog_name):
    post = api.one_object(blog_name)
    return template('<h2>{{title}}</h2><br/><p>{{content}}</p>', content=post['object']['content'], title=post['object']['title'])

run(host='localhost', port=8080)