# Generated by Django 5.1.2 on 2024-10-25 08:43

import apps.user.managers
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Model id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('phone_number', models.CharField(help_text='User phone number', max_length=20, unique=True)),
                ('name', models.CharField(help_text='User name', max_length=128)),
                ('coins', models.PositiveIntegerField(default=0, help_text='User coins')),
                ('avatar', models.ImageField(help_text='User profile image', upload_to='avatars/')),
                ('username', models.CharField(blank=True, help_text='User telegram username', max_length=128, null=True)),
                ('telegram_id', models.CharField(blank=True, help_text='User telegram id', max_length=64, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', apps.user.managers.CustomUserManager()),
            ],
        ),
    ]
