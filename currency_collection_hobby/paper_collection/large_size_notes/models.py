from django.db import models
from django.utils import timezone

# Create your models here.
class largeSizeCurrencyVariety(models.Model):
    LARGE_SIZE_TYPE = [
        ('1', 'Gold Certificates'),
        ('2', 'Silver Certificates'),
        ('3', 'Legal Tender'),
        ('4', 'Federal Reserve Bank Note'),
        ('5', 'Federal Reserve Note'),
        ('6', 'Treasury or Coin Note'),
        ('7', 'National Bank Note'),
    ]

    DENOMINATION = [
        ('$1',  'One Dollars'),
        ('$2',  'Two Dollars'),
        ('$5',  'Five Dollars'),
        ('$10', 'Ten Dollars'),
        ('$20', 'Twenty Dollars'),
        ('$50', 'Fifty Dollars'),
        ('$50', 'Hundred Dollars'),
    ]
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100, default='2025')
    fr_number = models.IntegerField(default=0, help_text="Fr Number.")
    price_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='large_size_notes_inventory/')
    date_added = models.DateTimeField(default=timezone.now)
    denomination = models.CharField(max_length=5, choices=DENOMINATION)
    type = models.CharField(max_length=25, choices=LARGE_SIZE_TYPE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name
    