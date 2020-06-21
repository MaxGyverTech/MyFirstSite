# Generated by Django 3.0.6 on 2020-05-28 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curse_name', models.CharField(max_length=200, verbose_name='Сurse name')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('les_title', models.CharField(max_length=200, verbose_name='Lesson title')),
                ('les_descr', models.TextField(verbose_name='Lesson description')),
                ('les_youtubelink', models.CharField(max_length=250, verbose_name='Youtube link')),
                ('les_googlelink', models.CharField(max_length=250, verbose_name='Google disk link')),
                ('curse', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='posts.Curse', verbose_name='For curse....')),
            ],
        ),
    ]
