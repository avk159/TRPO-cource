# Generated by Django 3.1.3 on 2020-12-14 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0017_auto_20201214_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msgdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 14, 22, 14, 52, 639152)),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 14, 22, 14, 52, 638156)),
        ),
    ]
