# Generated by Django 5.1.2 on 2024-10-27 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_cart_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='item_price',
        ),
    ]