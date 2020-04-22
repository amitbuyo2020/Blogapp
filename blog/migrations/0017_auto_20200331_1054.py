# Generated by Django 3.0.4 on 2020-03-31 05:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20200330_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='posted_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 5, 9, 2, 488661, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='heading',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 5, 9, 2, 491664, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 5, 9, 2, 484658, tzinfo=utc)),
        ),
    ]
