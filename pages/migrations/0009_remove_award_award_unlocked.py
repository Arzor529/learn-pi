# Generated by Django 3.0.2 on 2020-02-22 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20200220_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='award',
            name='award_unlocked',
        ),
    ]
