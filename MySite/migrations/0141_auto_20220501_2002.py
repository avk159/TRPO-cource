# Generated by Django 3.1.3 on 2022-05-01 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0140_auto_20220501_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='name',
        ),
        migrations.AlterField(
            model_name='appoint',
            name='appointreg',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 1, 20, 2, 31, 995200)),
        ),
        migrations.AlterField(
            model_name='person',
            name='login',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 1, 20, 2, 31, 994203)),
        ),
    ]
