# Generated by Django 3.0.4 on 2020-03-27 09:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_pic', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('bio_data', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('date_joined', models.DateTimeField(default=datetime.datetime(2020, 3, 27, 9, 14, 56, 875596, tzinfo=utc))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]