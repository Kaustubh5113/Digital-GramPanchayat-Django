# Generated by Django 5.1.3 on 2025-03-21 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egramApp', '0036_alter_death_date_of_issue_alter_event_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
        migrations.AlterField(
            model_name='death',
            name='date_of_issue',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 21, 21, 58, 12, 818652)),
        ),
    ]
