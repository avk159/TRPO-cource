from django.db import models
from datetime import datetime

# Класс пользователя
class Person(models.Model):
    name = models.CharField(max_length=20)
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20, null=False)
    usertype = models.BooleanField(default=False)
    registered = models.DateTimeField(default=datetime.now())

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['login', 'password'], name='unique_user'),
        ]

# Врачебные специальности
class docprofile(models.Model):
    profile = models.CharField(max_length=20)

# Класс врача
class Doctor(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)
    profile = models.ForeignKey(docprofile, on_delete=models.DO_NOTHING)

# Класс пациента
class Patient(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)

# Класс встречи/записи к врачу
class Appoint(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    appointdate = models.DateField()
    appointtime = models.TimeField(default='00:00')
    appointreg = models.DateTimeField(default=datetime.now(), blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['doctor', 'patient', 'appointdate', 'appointtime'], name='unique appointment'),
            models.UniqueConstraint(fields=['doctor', 'appointdate', 'appointtime'], name='unique_appdoc'),
            models.UniqueConstraint(fields=['patient', 'appointdate', 'appointtime'], name='unique_apppatient')
        ]

# Create your models here.