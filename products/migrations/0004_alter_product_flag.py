# Generated by Django 3.2 on 2022-08-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('sale', 'sale'), ('old', 'old'), ('new', 'new'), ('feature', 'feature')], max_length=10, verbose_name='Flag'),
        ),
    ]