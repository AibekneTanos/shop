from django.contrib import admin
from .models import Dish, Category, Company, Cart, CartContent


admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Cart)
admin.site.register(CartContent)

    #admin.site.register(Dish)
# Register your models here.


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_categories' , 'dish_type']
