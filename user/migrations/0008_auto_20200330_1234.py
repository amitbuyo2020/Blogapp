# Generated by Django 3.0.4 on 2020-03-30 06:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200329_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 30, 6, 49, 1, 411142, tzinfo=utc)),
        ),
    ]
