from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import FractionalCurrencyVariety

# Create your views here.
def fractional_currency(request):
    fractionCurrencies = FractionalCurrencyVariety.objects.all()
    return render(request, 'currency/fractional_currency.html', { 'fractionals': fractionCurrencies })

def fractional_currency_details(request, fractional_currency_id):
    currency = get_object_or_404(FractionalCurrencyVariety, pk=fractional_currency_id)
    return render(request, 'currency/fractional_currency_details.html', { 'fractional': currency })