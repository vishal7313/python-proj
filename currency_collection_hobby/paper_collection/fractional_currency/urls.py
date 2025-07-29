from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_fractional, name='all_fractional'),
    path('<int:fractional_id>/', views.fractional_details, name='fractional_detail'),
]