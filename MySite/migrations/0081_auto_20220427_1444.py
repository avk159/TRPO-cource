# Generated by Django 3.1.3 on 2022-04-27 07:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0080_auto_20220427_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint',
            name='appointreg',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 27, 14, 44, 36, 686838)),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 27, 14, 44, 36, 685824)),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('login', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MySite.person')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('login', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('profile', models.CharField(default='', max_length=20)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MySite.person')),
            ],
         ),
        #migrations.AddField(
        #    model_name='appoint',
        #    name='pat',
        #    field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MySite.patient'),
        #),

        #migrations.AddField(
        #    model_name='patient',
        #    name='id',
        #    field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
        #)
       # migrations.AlterField(
       #     model_name='appoint',
       #     name='doc',
       #     field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MySite.doctor'),
       # ),
    ]
