# Generated by Django 3.0.4 on 2020-03-27 07:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200327_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 7, 44, 44, 506481, tzinfo=utc)),
        ),
    ]
