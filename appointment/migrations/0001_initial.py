# Generated by Django 5.1.2 on 2024-10-26 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('car_brand', models.CharField(max_length=50)),
                ('car_model', models.CharField(max_length=50)),
                ('car_number', models.CharField(max_length=20)),
                ('services', models.JSONField()),
            ],
        ),
    ]