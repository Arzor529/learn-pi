# Generated by Django 3.0.2 on 2020-03-01 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0028_auto_20200301_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='awardunlocked',
            name='award_chosen',
        ),
        migrations.AddField(
            model_name='award',
            name='award_score',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
