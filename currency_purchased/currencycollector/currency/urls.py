from django.urls import path
from . import views

urlpatterns = [
    path('', views.fractional_currency, name='fractional_currency'),
    path('<int:fractional_currency_id>/', views.fractional_currency_details, name='fractional_currency_details'),
]