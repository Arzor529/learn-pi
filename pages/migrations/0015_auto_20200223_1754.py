# Generated by Django 3.0.2 on 2020-02-23 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20200223_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='award',
            name='lesson_complete',
        ),
        migrations.DeleteModel(
            name='LessonComplete',
        ),
    ]
