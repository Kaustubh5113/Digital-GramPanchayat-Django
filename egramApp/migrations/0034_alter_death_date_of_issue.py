# Generated by Django 5.1.3 on 2025-03-21 05:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egramApp', '0033_panchayatmember_alter_death_date_of_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='death',
            name='date_of_issue',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 21, 10, 31, 19, 608037)),
        ),
    ]
