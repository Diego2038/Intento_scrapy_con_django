# Generated by Django 4.2.1 on 2023-06-12 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_scrapy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='descripcion',
        ),
    ]
