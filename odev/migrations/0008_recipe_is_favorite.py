# Generated by Django 2.0.13 on 2019-05-12 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odev', '0007_auto_20190510_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='is_favorite',
            field=models.IntegerField(choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1),
        ),
    ]
