# Generated by Django 3.1.4 on 2021-08-24 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handling', '0009_auto_20210812_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
            ],
        ),
    ]
