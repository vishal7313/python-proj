from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_largesize_notes, name='all_large_size_notes'),
]