# Generated by Django 3.2 on 2022-09-21 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import utils.genrate_code


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPhoneNumper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numper', models.CharField(max_length=15)),
                ('type', models.CharField(choices=[('Academy', 'Academy'), ('Other', 'Other'), ('Home', 'Home'), ('Office', 'Office')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_phone', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Academy', 'Academy'), ('Other', 'Other'), ('Home', 'Home'), ('Office', 'Office')], max_length=10)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=80)),
                ('notes', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_adress', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profiel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='user')),
                ('code', models.CharField(default=utils.genrate_code.generate_code, max_length=15)),
                ('code_used', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profiel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
