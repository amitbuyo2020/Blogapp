# Generated by Django 3.0.4 on 2020-03-28 05:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200327_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 5, 10, 53, 99769, tzinfo=utc)),
        ),
    ]
