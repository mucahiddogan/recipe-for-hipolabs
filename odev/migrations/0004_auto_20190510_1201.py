# Generated by Django 2.0.13 on 2019-05-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odev', '0003_auto_20190509_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(choices=[('EASY', 'Easy'), ('NORMAL', 'Normal'), ('HARD', 'Hard')], max_length=45),
        ),
    ]