# Generated by Django 3.1.3 on 2022-04-27 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0097_auto_20220427_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint',
            name='appointreg',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 27, 18, 54, 20, 736801)),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 27, 18, 54, 20, 736801)),
        ),
    ]
