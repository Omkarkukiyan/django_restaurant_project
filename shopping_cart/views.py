from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from items.views import menu
from accounts.models import Profile
from items.models import FoodProducts
from shopping_cart.models import OrderItem, Order


def get_user_pending_order(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0

@login_required
def add_to_cart(request, **kwargs):
    user_profile = get_object_or_404(Profile, user=request.user)
    product = FoodProducts.objects.filter(id=kwargs.get('item_id', "")).first()
    if product in request.user.profile.fooditems.all():
        messages.info(request, "You already ordered this food")
        return redirect(reverse('items:menu'))
    order_item, status = OrderItem.objects.get_or_create(product=product)
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        user_order.save()

    messages.info(request, "Item added to cart")
    return redirect('menu')      


@login_required
def delete_from_cart(request, id):
    item_to_delete = OrderItem.objects.filter(pk=id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Your item has been deleted")
    return redirect('order_details')        



@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'cart/order.html', context)

