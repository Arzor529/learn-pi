# Generated by Django 3.0.2 on 2020-02-24 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_auto_20200223_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='award_desc_locked',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]