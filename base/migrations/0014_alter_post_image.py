# Generated by Django 4.1.6 on 2023-03-21 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
