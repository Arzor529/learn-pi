# Generated by Django 3.0.2 on 2020-02-20 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20200204_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award', models.CharField(max_length=255)),
                ('award_unlocked', models.BooleanField(default=False)),
                ('lesson_complete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Lesson')),
            ],
        ),
    ]
