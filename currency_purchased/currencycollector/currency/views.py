from django.shortcuts import render

# Create your views here.
def all_currency(request):
    return render(request, 'currency/all_currency.html')
