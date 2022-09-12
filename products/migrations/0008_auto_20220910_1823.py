# Generated by Django 3.2 on 2022-09-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20220910_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('sale', 'sale'), ('new', 'new'), ('old', 'old'), ('feature', 'feature')], max_length=10, verbose_name='Flag'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='prodect-image/', verbose_name='Image'),
        ),
    ]
