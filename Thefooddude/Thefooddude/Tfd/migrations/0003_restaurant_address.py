# Generated by Django 3.1.3 on 2020-12-23 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tfd', '0002_restaurant_res_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(default='', max_length=500),
        ),
    ]
