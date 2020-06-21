# Generated by Django 3.0.6 on 2020-05-28 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_curse_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curse',
            name='buyer',
        ),
        migrations.AddField(
            model_name='curse',
            name='curse_cost',
            field=models.IntegerField(default=0, verbose_name='Cost'),
        ),
        migrations.AddField(
            model_name='curse',
            name='curse_descr',
            field=models.TextField(default='Опсиание', verbose_name='Curse description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CurseBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Curse')),
            ],
        ),
    ]