# Generated by Django 5.1.2 on 2024-10-27 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_productsize_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsize',
            name='name_ru',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='productsize',
            name='name_uz',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
