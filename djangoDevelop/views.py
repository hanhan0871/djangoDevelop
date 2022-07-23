# Coding UTF-8
from django.http import HttpResponse


def demo1(request):
    return HttpResponse("hello world")


def demo2(request, data):
    return HttpResponse(data)


def demo3(request, x, y):
    m = int(x) * y
    return HttpResponse("the product is :" + str(m))