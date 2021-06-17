from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    country = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.country


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    locations = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username


class Company(models.Model):

    title = models.CharField(max_length=150)

    def __str__(self):

        return self.title


class Category(models.Model):
    # CharField, IntegerField FloatField и другие- это поля модели
    title = models.CharField(max_length=100, verbose_name='Название Категории', help_text='введите название Категория')
    description = models.CharField(max_length=500, verbose_name='Описание')

    # возвращение дефолтного значения при обращении к обьекту
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Dish(models.Model):
    image = models.ImageField(upload_to='images/', null=True, verbose_name='Картинка', max_length=900)
    title = models.CharField(max_length=100, verbose_name='Название блюда', help_text='Введите название блюда')
    dish_type = models.CharField(max_length=100, verbose_name='Тип блюда')
    description = models.CharField(max_length=500, verbose_name='Описание')
    categories = models.ManyToManyField(Category, verbose_name='категория')
    company = models.ForeignKey(Company, verbose_name='компания', on_delete=models.SET_NULL, null=True, default=2)
    price = models.PositiveIntegerField(verbose_name='цена')


    def get_categories(self):
        return ', '.join([cat.title for cat in self.categories.all()])

    get_categories.short_description = "Категории"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class Cart(models.Model):
    session_key = models.CharField(max_length=999, blank=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    total_cost = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)

    def get_total(self):
        items = CartContent.objects.filter(cart=self.id)
        total = 0
        for item in items:
            total += item.product.price * item.qty
        return total

    def get_cart_content(self):
        item = CartContent.objects.all()
        return item


class CartContent(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Dish, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(null=True)


class Kit(models.Model):
    total_before = models.PositiveIntegerField(default=0)
    total_after = models.PositiveIntegerField(default=0)
    items = models.ManyToManyField(Dish)
    percent = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(99)])

    def __str__(self):
        return str(self.id)





