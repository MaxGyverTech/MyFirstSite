# Generated by Django 3.0.6 on 2020-06-13 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20200606_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurseLanding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presimage', models.ImageField(blank=True, default=None, upload_to='images/landing/', verbose_name='Пресент картинка')),
                ('maindescription', models.TextField(verbose_name='Втрое описание')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Curse')),
            ],
            options={
                'verbose_name': 'Лендинг',
                'verbose_name_plural': 'Лендинги',
            },
        ),
        migrations.CreateModel(
            name='CurseLandingAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.TextField(verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.CurseLanding')),
            ],
            options={
                'verbose_name': 'Вопрос ответ',
                'verbose_name_plural': 'Вопрос ответ',
            },
        ),
    ]
