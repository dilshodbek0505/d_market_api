# Generated by Django 5.1.2 on 2024-10-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_productsize_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsize',
            name='name',
            field=models.FloatField(),
        ),
    ]
