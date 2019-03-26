
# Django
from django.http import HttpResponse

# utilities
from datetime import datetime

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! current server time  is {now}'.format(now=str(now)))
    # return HttpResponse('<h1>Hello, world</h1>')

# def hi(request):
#     return HttpResponse('Hi!!')
