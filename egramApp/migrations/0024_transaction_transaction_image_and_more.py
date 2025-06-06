# Generated by Django 5.1.3 on 2025-02-06 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egramApp', '0023_hometax_alter_death_date_of_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_image',
            field=models.ImageField(blank=True, null=True, upload_to='transactions/'),
        ),
        migrations.AlterField(
            model_name='death',
            name='date_of_issue',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 6, 12, 41, 35, 49899)),
        ),
    ]
