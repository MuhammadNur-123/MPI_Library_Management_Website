# Generated by Django 5.0.6 on 2024-09-05 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_is_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
    ]
