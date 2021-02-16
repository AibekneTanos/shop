from django.contrib import admin
from .models import Dish
from .models import Vino

#admin.site.register(Dish)
# Register your models here.
@admin.register(Vino)
class Vino(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'dish_type']
