# Generated by Django 4.1.1 on 2022-10-04 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slider/%Y/%m/%d')),
                ('link', models.URLField(blank=True, verbose_name='ссылка')),
            ],
            options={
                'verbose_name': 'Слайдер. Главная страница',
                'verbose_name_plural': 'Слайдер. Главная страница',
            },
        ),
    ]
