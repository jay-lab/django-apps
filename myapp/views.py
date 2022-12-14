from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
import random
# Create your views here.

topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'Model', 'body':'Model is ..'},
]

def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return HttpResponse(f'''
    <html>
    <body>
        <h1><a href='/'>Django</h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
    </body>
    </html>
    ''')

def index(request):
    # return HttpResponse('Welcome!')
    # return HttpResponse('<h1>Random</h1>' + str(random.random()))
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def create(request):
    return HttpResponse('create!')

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))