# Generated by Django 3.0.2 on 2020-02-23 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20200223_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='user',
        ),
        migrations.AddField(
            model_name='award',
            name='lesson_complete',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages.Lesson'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_complete',
            field=models.BooleanField(default=False),
        ),
    ]