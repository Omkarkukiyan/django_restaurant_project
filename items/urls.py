from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('<int:id>/', views.single_product, name='single_product'),
]    
