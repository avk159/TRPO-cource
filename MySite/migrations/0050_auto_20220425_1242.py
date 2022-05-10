# Generated by Django 3.1.3 on 2022-04-25 05:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0049_auto_20220421_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='appoint',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='appoint',
            name='appointreg',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 25, 12, 42, 26, 360867)),
        ),
        migrations.AlterField(
            model_name='message',
            name='msgdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 25, 12, 42, 26, 360867)),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 25, 12, 42, 26, 360867)),
        ),
        migrations.AlterUniqueTogether(
            name='appoint',
            unique_together=set(),
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
        migrations.AlterModelTable(
            name='appoint',
            table='MySite_appoint',
        ),
    ]
