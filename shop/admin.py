from django.contrib import admin
from .models import Dish, Company, Cart, CartContent, Category, Kit, UserProfile, Location
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartContent)
admin.site.register(Kit)

    #admin.site.register(Dish)
# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'locations']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["id", "country"]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'dish_type', 'price', ]


