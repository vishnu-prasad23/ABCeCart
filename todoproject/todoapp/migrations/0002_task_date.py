# Generated by Django 3.2.16 on 2023-01-13 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-02-21'),
            preserve_default=False,
        ),
    ]
