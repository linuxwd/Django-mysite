# encoding: utf-8


from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response

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
    return render_to_response('math.html', locals())
def menu(request):
    """retrun a menu response

    :request: client request
    :returns: http response

    """
    food1 = {'name': '番茄炒蛋', 'price': 60, 'comment': '好吃', 'is_spicy': False}
    food2 = {'name': '蒜泥白肉', 'price': 100, 'comment': '人氣推薦', 'is_spicy': True}
    foods = [food1, food2]
    return render_to_response('menu.html', locals())