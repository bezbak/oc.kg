# Generated by Django 4.1.3 on 2022-12-09 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_alter_about_us_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='logo',
            field=models.FileField(upload_to='logo/'),
        ),
    ]