# Generated by Django 3.2 on 2022-11-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20221118_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useradress',
            name='type',
            field=models.CharField(choices=[('Other', 'Other'), ('Home', 'Home'), ('Office', 'Office'), ('Academy', 'Academy')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userphonenumper',
            name='type',
            field=models.CharField(choices=[('Other', 'Other'), ('Home', 'Home'), ('Office', 'Office'), ('Academy', 'Academy')], max_length=10),
        ),
    ]
