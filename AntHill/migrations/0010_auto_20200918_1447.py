# Generated by Django 3.1 on 2020-09-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AntHill', '0009_auto_20200918_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='rikka4.jpg', upload_to='avatars'),
        ),
    ]