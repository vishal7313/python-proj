from django.db import models
from django.utils import timezone

# Create your models here.
class FractionalCurrencyVariety(models.Model):
    ISSUE_TYPE = [
        ('I', 'First Issue'),
        ('II', 'Second Issue'),
        ('III', 'Third Issue'),
        ('IV', 'Fourth Issue'),
        ('V', 'Fifth Issue'),
    ]
    CURRENCY_TYPE_CHOICE = [
        ('III', 'Three Cents'),
        ('V', 'Five Cents'),
        ('X', 'Ten Cents'),
        ('XXV', 'Twenty Five Cents'),
        ('L', 'Fifty Cents'),
    ]
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100, default='2025')
    fr_number = models.IntegerField(default=0, help_text="Fr Number.")
    price_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='fractioanl_currencies/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=5, choices=CURRENCY_TYPE_CHOICE)
    issue = models.CharField(max_length=5, choices=ISSUE_TYPE)
    
    def __str__(self):
        return self.name

    
    