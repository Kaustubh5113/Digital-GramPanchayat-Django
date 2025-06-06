# Generated by Django 5.1.3 on 2025-01-31 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egramApp', '0022_alter_death_date_of_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeTax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_date', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid')], max_length=20)),
                ('screenshot', models.ImageField(blank=True, null=True, upload_to='screenshots/')),
            ],
        ),
        migrations.AlterField(
            model_name='death',
            name='date_of_issue',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 31, 19, 39, 11, 968570)),
        ),
    ]
