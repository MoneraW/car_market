# Generated by Django 2.0.6 on 2018-07-24 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_car_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
