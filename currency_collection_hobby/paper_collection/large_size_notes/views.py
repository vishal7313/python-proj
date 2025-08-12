from django.shortcuts import render
from .models import largeSizeCurrencyVariety
from django.shortcuts import render, get_list_or_404, get_object_or_404

# Create your views here.
def all_largesize_notes(request):
    largenotes = largeSizeCurrencyVariety.objects.all()
    return render(request, 'large_size_notes/all_large_size.html', { 'largenotes': largenotes })

def largesize_details(request, largesize_id):
    largenote = get_object_or_404(largeSizeCurrencyVariety, pk=largesize_id)
    return render(request, 'large_size_notes/largesize_note_detail.html', { 'largesizenote': largenote })