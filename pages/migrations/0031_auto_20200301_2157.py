# Generated by Django 3.0.2 on 2020-03-01 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0030_friend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='friend',
        ),
        migrations.AddField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Friend', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]