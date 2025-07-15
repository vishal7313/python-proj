from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello World. You are at my personal collection home page")

def about(request):
    return HttpResponse("Hello World. You are at my personal collection about page")

def contact(request):
    return HttpResponse("Hello World. You are at my personal collection contact page")