# Generated by Django 3.1 on 2020-09-15 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AntHill', '0004_auto_20200914_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
