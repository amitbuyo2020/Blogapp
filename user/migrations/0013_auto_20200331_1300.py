# Generated by Django 3.0.4 on 2020-03-31 07:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20200331_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 7, 15, 27, 170473, tzinfo=utc)),
        ),
    ]