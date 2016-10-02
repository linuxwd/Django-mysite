# encoding: utf-8


from django.http import HttpResponse

def here(request):
    return HttpResponse('妈，我在这 ! ')

def add(request,a,b):
    s = int(a) + int(b)
    return HttpResponse(str(s))