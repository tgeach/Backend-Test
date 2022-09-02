from django.urls import path
from . import views

urlpatterns = [
    path('donations/', views.donation_list, name='donations'),
    path('donations/<int:id>', views.donation_detail, name='detail')
]