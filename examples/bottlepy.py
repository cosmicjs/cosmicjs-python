from bottle import route, run, template
from pythoncosmicjs import Api
api = Api('pythoncosmicjs')


@route('/')
def index():
    post_list = api.all_objects_json()
    id_post = 0
    while 10 < id_post:
        title = post_list['objects'][0]['title']
        id_post += 1
    return template('<a href="{{url}}">{{title}}</a>', title=post_list['objects'][0]['title'], url=post_list['objects'][0]['slug'])


@route('/<blog_name>')
def blog(blog_name):
    post = api.object_json(blog_name)
    return template('<h2>{{title}}</h2><br/><p>{{content}}</p>', content=post['object']['content'], title=post['object']['title'])

run(host='localhost', port=8080)