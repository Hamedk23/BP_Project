# Generated by Django 3.1.7 on 2021-03-07 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20210307_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 7, 14, 34, 51, 353788), verbose_name='Time submited'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='timelimit',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='timeuploded',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 7, 14, 34, 51, 353517)),
        ),
    ]
