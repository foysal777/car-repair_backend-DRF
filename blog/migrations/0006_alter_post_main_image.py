# Generated by Django 5.0.6 on 2025-07-17 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_gallery_image_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='main_image',
            field=models.CharField(default='', max_length=944),
        ),
    ]
