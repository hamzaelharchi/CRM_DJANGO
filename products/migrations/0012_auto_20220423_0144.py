# Generated by Django 3.1.14 on 2022-04-23 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]