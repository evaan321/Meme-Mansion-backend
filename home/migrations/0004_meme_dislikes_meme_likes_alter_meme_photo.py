# Generated by Django 4.2.7 on 2024-04-30 11:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_alter_meme_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='disliked_memes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meme',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_memes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meme',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
