# Generated by Django 4.1.3 on 2023-02-23 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_watchedmovie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile_image/102806976_t1kbCQj.jpg', null=True, upload_to='profile_image/'),
        ),
    ]