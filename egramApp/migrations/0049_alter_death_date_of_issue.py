# Generated by Django 5.2 on 2025-04-06 19:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egramApp', '0048_villagepopulation_delete_emergencycontact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='death',
            name='date_of_issue',
            field=models.DateTimeField(default=datetime.datetime(2025, 4, 7, 0, 36, 34, 195677)),
        ),
    ]
