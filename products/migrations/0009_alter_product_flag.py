# Generated by Django 3.2 on 2022-09-12 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20220910_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('feature', 'feature'), ('sale', 'sale'), ('old', 'old'), ('new', 'new')], max_length=10, verbose_name='Flag'),
        ),
    ]
