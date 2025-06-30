from django.shortcuts import render
from .models import FractionalCurrencyVariety

# Create your views here.
def all_currency(request):
    fractionCurrencies = FractionalCurrencyVariety.objects.all()
    return render(request, 'currency/all_currency.html', { 'fractionals': fractionCurrencies })
