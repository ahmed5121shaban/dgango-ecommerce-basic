# Generated by Django 3.2 on 2022-08-23 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220823_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=1, verbose_name='Price'),
        ),
    ]
