# Generated by Django 3.0.6 on 2020-05-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200528_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='curse',
            name='curse_img',
            field=models.ImageField(default=None, upload_to='', verbose_name='Image'),
        ),
    ]