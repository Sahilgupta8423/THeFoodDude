# Generated by Django 3.1.3 on 2021-01-02 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tfd', '0008_auto_20210101_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('help_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=111)),
                ('phone', models.CharField(max_length=111)),
                ('address', models.CharField(max_length=111)),
                ('city', models.CharField(max_length=111)),
            ],
        ),
    ]