from django.urls import path

from . import views

urlpatterns = [
    path('cart/', views.order_details, name="order_details"),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('item/delete/<int:id>/', views.delete_from_cart, name='delete_from_cart')
]    
