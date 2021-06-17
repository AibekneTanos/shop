from cart import cart
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, m2m_changed, pre_save
from django.dispatch import receiver
from shop.models import UserProfile, Kit, Dish, Company, CartContent


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=Dish.company)
def create_dish(instance, **kwargs):
    if instance.company.id == 4:
        instance.company.title = Company.objects.get(id=6)
        instance.company.save()


post_save.connect(create_dish, sender=Dish.company)




def create_kit(instance, **kwargs):
    if kwargs["action"] == 'post_add':
        if instance.items.count() < 2:
            raise ValidationError(f'You cant assign less than two regions, now {instance.items.count()}')
        total = 0
        for item in instance.items.all():
            total += item.price

        instance.total_before = total
        if instance.total_after == 0:
            instance.total_after = total * (100 - instance.percent)/100

        else:
            instance.percent = (instance.total_after / instance.total_before) * 100

        instance.save()


m2m_changed.connect(create_kit, sender=Kit.items.through)




