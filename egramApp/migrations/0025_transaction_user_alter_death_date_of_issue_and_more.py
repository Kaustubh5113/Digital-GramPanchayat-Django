# Generated by Django 5.1.3 on 2025-02-06 09:30

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egramApp', '0024_transaction_transaction_image_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='death',
            name='date_of_issue',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 6, 15, 0, 20, 799633)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]
