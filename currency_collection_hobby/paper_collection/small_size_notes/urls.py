from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_smallsize_notes, name='all_small_size_notes'),
    path('<int:smallsize_id>/', views.smallsize_details, name='smallnote_detail'),
]