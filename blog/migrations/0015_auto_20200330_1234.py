# Generated by Django 3.0.4 on 2020-03-30 06:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200329_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 30, 6, 49, 1, 373119, tzinfo=utc)),
        ),
    ]
