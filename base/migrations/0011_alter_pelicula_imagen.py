# Generated by Django 4.1.6 on 2023-03-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_pelicula_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
