# encoding: utf-8


from django.http import HttpResponse
from django import template
from django.template.loader import get_template

def here(request):
    return HttpResponse('妈，我在这 ! ')

def add(request,a,b):
    s = int(a) + int(b)
    return HttpResponse(str(s))
def math(request,a,b):
    a = int(a)
    b = int(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    t = get_template('math.html')
    c = template.Context({'s': s, 'd': d, 'p': p, 'q': q})
    return HttpResponse(t.render(c))