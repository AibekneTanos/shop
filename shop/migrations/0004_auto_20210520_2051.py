# Generated by Django 3.1.6 on 2021-05-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_cart_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='categories',
            field=models.ManyToManyField(null=True, to='shop.Category', verbose_name='категория'),
        ),
    ]
