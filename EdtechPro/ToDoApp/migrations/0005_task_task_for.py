# Generated by Django 3.2.9 on 2021-11-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0004_auto_20211123_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_for',
            field=models.CharField(default='DEFAULT', max_length=32),
            preserve_default=False,
        ),
    ]
