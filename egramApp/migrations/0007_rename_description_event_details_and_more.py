# Generated by Django 5.1.3 on 2024-12-28 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egramApp', '0006_alter_death_date_of_issue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='description',
            new_name='details',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
        migrations.AddField(
            model_name='event',
            name='short_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='death',
            name='date_of_issue',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 28, 23, 20, 2, 181751)),
        ),
    ]
