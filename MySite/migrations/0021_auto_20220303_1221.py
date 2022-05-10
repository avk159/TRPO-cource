# Generated by Django 3.1.3 on 2022-03-03 05:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0020_auto_20201214_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='appoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=20)),
                ('patient', models.CharField(max_length=20)),
                ('appointreg', models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 3, 12, 21, 28, 164953))),
                ('appointdate', models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 3, 12, 21, 28, 164953))),
                ('appointtime', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='typedoctor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='msgdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 3, 12, 21, 28, 164953)),
        ),
        migrations.AlterField(
            model_name='person',
            name='crypt',
            field=models.CharField(default='1', max_length=8),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 3, 12, 21, 28, 164953)),
        ),
    ]
