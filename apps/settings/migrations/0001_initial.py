# Generated by Django 4.1.3 on 2022-11-19 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500, verbose_name='О нас текст')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название рекламы')),
                ('image', models.ImageField(upload_to='ads_image/', verbose_name='Фото рекламы')),
                ('link', models.URLField(verbose_name='Ссылка рекламы')),
            ],
            options={
                'verbose_name': 'Реклама',
                'verbose_name_plural': 'Рекламы',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('logo', models.ImageField(upload_to='logo/')),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.URLField(blank=True, max_length=50, null=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, max_length=50, null=True, verbose_name='instagram')),
                ('twitter', models.URLField(blank=True, max_length=50, null=True, verbose_name='twitter')),
                ('vk', models.URLField(blank=True, max_length=50, null=True, verbose_name='vk')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]