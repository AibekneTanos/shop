# Generated by Django 3.1.6 on 2021-06-08 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210607_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='dish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.dish', verbose_name='блюдо'),
        ),
    ]