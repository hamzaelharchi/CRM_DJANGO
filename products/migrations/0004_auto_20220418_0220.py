# Generated by Django 3.1.14 on 2022-04-18 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='images/products/product-default.png', upload_to='images/products'),
        ),
    ]