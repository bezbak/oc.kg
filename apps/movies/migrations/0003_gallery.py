# Generated by Django 4.1.3 on 2022-12-10 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_comments_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='gallery/')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='movies.movie')),
            ],
        ),
    ]
