# Generated by Django 3.1 on 2020-09-18 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AntHill', '0006_auto_20200915_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, to='AntHill.Category'),
        ),
    ]
