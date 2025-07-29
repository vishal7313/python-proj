from django.shortcuts import render
from .models import fractionalCurrencyVariety
from django.shortcuts import render, get_list_or_404, get_object_or_404

# Create your views here.
def all_fractional(request):
    fractionals = fractionalCurrencyVariety.objects.all()
    return render(request, 'fractional_currency/all_fractional.html', { 'fractionals': fractionals })

def fractional_details(request, fractional_id):
    fractional = get_object_or_404(fractionalCurrencyVariety, pk=fractional_id)
    return render(request, 'fractional_currency/fractional_currency_detail.html', { 'fractional': fractional })