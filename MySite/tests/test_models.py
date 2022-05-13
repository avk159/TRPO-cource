from django.test import TestCase
from MySite.models import Person, Appoint, Doctor, Patient, docprofile
from datetime import datetime, time
# Create your tests here.

# Тестирование полей модели Person мок
class PersonModelTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        cls.person = Person.objects.create(
            name = "Анастасия",
            login = "Nastysha",
            password = "nasty123",
            usertype = False,
            registered = datetime.now()

        )

    # 1 тестирование полей
    def test_it_has_information_fields(self):
        self.assertIsInstance(self.person.name, str)
        self.assertIsInstance(self.person.login, str)
        self.assertIsInstance(self.person.password, str)
        self.assertIsInstance(self.person.usertype, bool)
        self.assertIsInstance(self.person.registered, datetime)

# Тестирование полей модели docprofile
class docprofileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.profile = docprofile.objects.create(profile="терапевт")

    # 2 тестирование полей
    def test_it_has_information_fields(self):
        self.assertIsInstance(self.profile.profile, str)

# Тестирование полей модели Doctor
class DoctorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        docprofile.objects.create(id=15, profile="Отоларинголог")
        Person.objects.create(id=21, name="Elena", login="Hehelena", password="14231423", registered=datetime.now())
        cls.doc = Doctor.objects.create(
            user=Person.objects.get(id=21),
            profile=docprofile.objects.get(id=15),
        )

    # 3 тестирование полей
    def test_it_has_information_fields(self):
        self.assertIsInstance(self.doc.user, Person)
        self.assertIsInstance(self.doc.profile, docprofile)

# Тестирование полей модели Пациент
class PatientModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Person.objects.create(id=23, name="Daniel", login="Hehelena", password="1423", registered=datetime.now())
        cls.pat = Patient.objects.create(
            user=Person.objects.get(id=23),
        )

    # 4 тестирование полей
    def test_it_has_information_fields(self):
        self.assertIsInstance(self.pat.user, Person)

# Тестирование полей модели Appoint
class AppointModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        docprofile.objects.create(id=16, profile="Отоларинголог")
        Person.objects.create(id=1, name="Vasya", login="Vasyugan", password="123456", registered = datetime.now())
        Person.objects.create(id=2, name="Elena", login="Hehelena", password="14231423", registered=datetime.now())
        cls.appoint = Appoint.objects.create(
            doctor = Doctor.objects.create(user_id=1, profile_id=16),
            patient = Patient.objects.create(user_id=2),
            appointdate = datetime(2022, 6 ,13),
            appointtime = "09:00",
            appointreg = datetime.now(),
        )

    # 5 тестирование полей
    def test_it_has_information_fields(self):
        self.assertIsInstance(self.appoint.doctor, Doctor)
        self.assertIsInstance(self.appoint.patient, Patient)
        self.assertIsInstance(self.appoint.appointdate, datetime)
        self.assertIsInstance(self.appoint.appointtime, str)
        self.assertIsInstance(self.appoint.appointreg, datetime)

    # 6 тестирование даты встречи
    def test_appointdate_future(self):
        # Appoint date today or future date. You can't make an appointment to a past date
        self.assertGreaterEqual(self.appoint.appointdate, datetime.now())
