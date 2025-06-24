from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_currency, name='all_currency'),
]