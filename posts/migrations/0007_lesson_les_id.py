# Generated by Django 3.0.6 on 2020-06-02 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_curse_curse_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='les_id',
            field=models.IntegerField(default=1, verbose_name='Lesson number'),
        ),
    ]
