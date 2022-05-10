# Generated by Django 3.1.3 on 2022-04-19 07:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0026_auto_20220419_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint',
            name='appointreg',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 19, 14, 10, 48, 945961)),
        ),
        migrations.AlterField(
            model_name='message',
            name='msgdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 19, 14, 10, 48, 945961)),
        ),
        migrations.AlterField(
            model_name='person',
            name='profile',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 19, 14, 10, 48, 945961)),
        ),
    ]
