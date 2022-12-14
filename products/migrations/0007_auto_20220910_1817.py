# Generated by Django 3.2 on 2022-09-10 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20220829_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(upload_to='brand/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('sale', 'sale'), ('feature', 'feature'), ('old', 'old'), ('new', 'new')], max_length=10, verbose_name='Flag'),
        ),
        migrations.AlterField(
            model_name='productsimages',
            name='image',
            field=models.ImageField(upload_to='prodect-image/', verbose_name='Image'),
        ),
    ]
