from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category_detail, name='manzil_list'),   
    path('manzil/<int:pk>/', views.manzil_detail, name='manzil_detail'),
]
