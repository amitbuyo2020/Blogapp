# Generated by Django 3.0.4 on 2020-03-30 06:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200330_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='posted_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 30, 6, 55, 2, 980994, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='heading',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 30, 6, 55, 2, 982995, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 30, 6, 55, 2, 976992, tzinfo=utc)),
        ),
    ]
