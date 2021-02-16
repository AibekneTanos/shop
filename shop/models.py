from django.db import models
from django.db import models


# Create your models here.
class Vino(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название напитка", help_text="Введите название напитка ")
    description = models.CharField(max_length=500, verbose_name="Описание")




class Dish(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название блюда', help_text='Введите название блюда')
    dish_type = models.CharField(max_length=100, verbose_name='Тип блюда')
    description = models.CharField(max_length=500, verbose_name='Описание')




def __str__(self):
    return self.title

