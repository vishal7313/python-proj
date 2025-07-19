from django.shortcuts import render

# Create your views here.
def all_fractional(request):
    return render(request, 'fractional_currency/all_fractional.html')