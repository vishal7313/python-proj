from django.shortcuts import render
from .models import smallSizeCurrencyVariety
from django.shortcuts import render, get_list_or_404, get_object_or_404

# Create your views here.
def all_smallsize_notes(request):
    smallnotes = smallSizeCurrencyVariety.objects.all()
    return render(request, 'small_size_notes/all_small_size.html', { 'smallnotes': smallnotes })

def smallsize_details(request, smallsize_id):
    smallnote = get_object_or_404(smallSizeCurrencyVariety, pk=smallsize_id)
    return render(request, 'small_size_notes/smallsize_note_detail.html', { 'smallsizenote': smallnote })