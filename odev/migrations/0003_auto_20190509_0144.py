# Generated by Django 2.0.13 on 2019-05-09 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odev', '0002_recipe_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
