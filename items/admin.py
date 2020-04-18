from django.contrib import admin

from .models import Category, FoodProducts

# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'section', 'price')
    list_display_links = ('id', 'name')
    list_filter = ('section',)
    search_fields = ('name',)
    list_per_page = 20

class CategoryAdmin(admin.ModelAdmin):
        list_display = ('id','section')

admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodProducts, FoodAdmin)