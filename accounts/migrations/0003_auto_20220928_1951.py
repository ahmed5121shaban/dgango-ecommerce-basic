# Generated by Django 3.2 on 2022-09-28 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220921_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useradress',
            name='type',
            field=models.CharField(choices=[('Academy', 'Academy'), ('Other', 'Other'), ('Home', 'Home'), ('Office', 'Office')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userphonenumper',
            name='type',
            field=models.CharField(choices=[('Academy', 'Academy'), ('Other', 'Other'), ('Home', 'Home'), ('Office', 'Office')], max_length=10),
        ),
    ]