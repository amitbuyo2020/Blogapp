# Generated by Django 3.0.4 on 2020-03-29 04:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200328_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 29, 4, 22, 34, 201259, tzinfo=utc)),
        ),
    ]
