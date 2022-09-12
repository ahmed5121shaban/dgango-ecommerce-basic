# Generated by Django 3.2 on 2022-09-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('feature', 'feature'), ('old', 'old'), ('new', 'new'), ('sale', 'sale')], max_length=10, verbose_name='Flag'),
        ),
    ]