from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')
    # return HttpResponse("Hello World. You are at my personal collection home page")

def about(request):
    return HttpResponse("Hello World. You are at my personal collection about page")

def contact(request):
    return HttpResponse("Hello World. You are at my personal collection contact page")