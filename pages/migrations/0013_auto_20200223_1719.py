# Generated by Django 3.0.2 on 2020-02-23 17:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0012_award_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='award',
            name='user',
        ),
        migrations.AddField(
            model_name='award',
            name='user',
            field=models.ManyToManyField(related_name='awards', to=settings.AUTH_USER_MODEL),
        ),
    ]
