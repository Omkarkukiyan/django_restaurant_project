from django.shortcuts import render
from .models import FoodProducts

# Create your views here.


def menu(request):
    menus = FoodProducts.objects.all().filter(section=1)
    deserts = FoodProducts.objects.all().filter(section=2)
    beverages = FoodProducts.objects.all().filter(section=3)
    coffees = FoodProducts.objects.all().filter(section=4)
    context = {
        'menus':menus,
        'deserts': deserts,
        'beverages' : beverages,
        'coffees' : coffees,
    }
    return render(request, 'items/menu.html', context)


def single_product(request, id):
    single_product = FoodProducts.objects.get(pk=id)
    context = {
        'single_product':single_product
    }
    return render(request, 'items/single-product.html', context)


