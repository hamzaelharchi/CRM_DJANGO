# Generated by Django 4.0.3 on 2022-05-15 06:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_userprofile_born'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='born',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='born date'),
        ),
    ]
