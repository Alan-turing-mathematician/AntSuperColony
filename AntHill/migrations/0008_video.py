# Generated by Django 3.1 on 2020-09-18 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AntHill', '0007_auto_20200918_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('video', embed_video.fields.EmbedVideoField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(blank=True, to='AntHill.Category')),
            ],
        ),
    ]
