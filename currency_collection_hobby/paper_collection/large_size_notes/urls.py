from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_largesize_notes, name='all_large_size_notes'),
    path('<int:largesize_id>/', views.largesize_details, name='largenote_detail'),
]