from django.urls import path

from . import views

urlpatterns = [
    path('payment-done/', views.charge, name='charge'),
    path('', views.checkout.as_view(), name='checkout')
   
    
]    
