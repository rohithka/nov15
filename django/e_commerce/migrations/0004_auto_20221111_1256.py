# Generated by Django 2.2.8 on 2022-11-11 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0003_auto_20221110_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartmodel',
            name='date',
        ),
        migrations.AlterField(
            model_name='checkoutmodel',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]