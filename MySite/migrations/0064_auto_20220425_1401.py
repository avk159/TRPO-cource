# Generated by Django 3.1.3 on 2022-04-25 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0063_auto_20220425_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=20)),
                ('patient', models.CharField(max_length=20)),
                ('appointdate', models.DateField()),
                ('appointtime', models.TimeField(default='00:00')),
                ('appointreg', models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 25, 14, 1, 21, 938710))),
                ('approved', models.BooleanField(blank=True, default=False)),
            ],
        ),
       # migrations.RemoveConstraint(
       #     model_name='message',
       #     name='unique appointment',
       # ),
       # migrations.RemoveConstraint(
       #     model_name='message',
       #     name='unique_appdoc',
       # ),
       # migrations.RemoveConstraint(
       #     model_name='message',
       #     name='unique_apppatient',
       # ),
        migrations.AlterField(
            model_name='message',
            name='msgdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 25, 14, 1, 21, 938710)),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 25, 14, 1, 21, 938710)),
        ),
        migrations.AddConstraint(
            model_name='appoint',
            constraint=models.UniqueConstraint(fields=('doctor', 'patient', 'appointdate', 'appointtime'), name='unique appointment'),
        ),
        migrations.AddConstraint(
            model_name='appoint',
            constraint=models.UniqueConstraint(fields=('doctor', 'appointdate', 'appointtime'), name='unique_appdoc'),
        ),
        migrations.AddConstraint(
            model_name='appoint',
            constraint=models.UniqueConstraint(fields=('patient', 'appointdate', 'appointtime'), name='unique_apppatient'),
        ),
    ]
