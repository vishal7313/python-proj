from django.db import models
from django.utils import timezone

# Create your models here.
class smallSizeCurrencyVariety(models.Model):
    SMALL_SIZE_TYPE = [
        ('Gold Certificates', 'Gold Certificates'),
        ('Silver Certificates', 'Silver Certificates'),
        ('Legal Tender', 'Legal Tender'),
        ('Federal Reserve Bank Note', 'Federal Reserve Bank Note'),
        ('Federal Reserve Note5', 'Federal Reserve Note'),
        ('Treasury or Coin Note', 'Treasury or Coin Note'),
        ('National Bank Note', 'National Bank Note'),
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
    serial_number = models.CharField(default='', max_length=32)
    price_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='small_size_notes_inventory/')
    date_added = models.DateTimeField(default=timezone.now)
    denomination = models.CharField(max_length=5, choices=DENOMINATION)
    type = models.CharField(max_length=25, choices=SMALL_SIZE_TYPE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name
    