from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world. I am making currency collection project.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello world. I am making currency collection project about.")

def contact(request):
    return HttpResponse("Hello world. I am making currency collection project contact.")
