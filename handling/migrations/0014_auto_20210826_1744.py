# Generated by Django 3.1.4 on 2021-08-26 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('handling', '0013_auto_20210825_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
        migrations.DeleteModel(
            name='Session',
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
