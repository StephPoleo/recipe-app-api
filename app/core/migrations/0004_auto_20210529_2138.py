# Generated by Django 2.1.15 on 2021-05-29 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_ingredient'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredient',
            new_name='Ingredients',
        ),
    ]
