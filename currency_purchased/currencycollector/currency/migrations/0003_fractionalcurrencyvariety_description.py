# Generated by Django 5.2.3 on 2025-06-29 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_fractionalcurrencyvariety_fr_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fractionalcurrencyvariety',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
