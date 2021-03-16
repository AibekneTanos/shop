from django.contrib import admin
from .models import Dish, Company, Cart, CartContent, Category

admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Cart)
admin.site.register(CartContent)

    #admin.site.register(Dish)
# Register your models here.


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'dish_type', 'price']


