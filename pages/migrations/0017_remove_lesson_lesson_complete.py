# Generated by Django 3.0.2 on 2020-02-23 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20200223_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='lesson_complete',
        ),
    ]