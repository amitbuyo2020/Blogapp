# Generated by Django 3.0.4 on 2020-03-27 07:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 7, 17, 58, 716234, tzinfo=utc)),
        ),
    ]
