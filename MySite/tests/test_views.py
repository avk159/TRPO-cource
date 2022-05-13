from django.test import TestCase, Client
from MySite.models import Person, Appoint
from django.urls import reverse
from MySite.views import *
from datetime import timedelta
from django.conf import settings
from importlib import import_module
# Create your tests here

# Тестирование отображения шаблонов
class PageLoadViewTest(TestCase):

    # установка сессии для теста
    def setUp(self):
        # http://code.djangoproject.com/ticket/10899
        settings.SESSION_ENGINE = 'django.contrib.sessions.backends.file'
        engine = import_module(settings.SESSION_ENGINE)
        store = engine.SessionStore()
        store.save()
        self.session = store
        self.client.cookies[settings.SESSION_COOKIE_NAME] = store.session_key

    # 1 страница авторизации
    def testViewAuthLoad(self):
        response = self.client.get(reverse('auth'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth.html')

    # 2 страница регистрации
    def testViewRegisterLoad(self):
        response = self.client.get(reverse('register'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    # 3 страница администратора
    def testViewAmdLoad(self):
        session = self.session
        session['person_id'] = 1
        session.save()

        person = Person.objects.create(id=1, name="Elena", login="Hehelena", password="14231423", usertype=False, registered=datetime.now())
        response = self.client.get(reverse('adminpage'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'adm.html')

    # 4 страница контактов
    def testViewContactsLoad(self):
        response = self.client.get(reverse('contacts'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    # 5 страница о сервисе
    def testViewAboutLoad(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'abouts.html')

    # 6 персональная страница пациента
    def testViewUserpagePatientLoad(self):
        session = self.session
        session['person_id'] = 2
        session.save()

        sessid = session['person_id']

        person1 = Person.objects.create(id=2, name="Elena", login="Hehelena", password="14231423", usertype=False, registered=datetime.now())
        person2 = Person.objects.create(id=6, name="Henry", login="Hehehe", password="12345", usertype=True,
                                        registered=datetime.now())
        docprofile.objects.create(id=2, profile="Отоларинголог")
        Doctor.objects.create(user_id=6, profile_id=2)
        Patient.objects.create(user_id=2)

        person = Person.objects.get(id=sessid)
        # тест
        response = self.client.get(reverse('userpage', kwargs={"id": sessid}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointment.html')

    # 7 персональная страница врача
    def testViewUserpageDoctorLoad(self):
        session = self.session
        session['person_id'] = 6
        session.save()

        sessid = session['person_id']

        person1 = Person.objects.create(id=2, name="Elena", login="Hehelena", password="14231423", usertype=False, registered=datetime.now())
        person2 = Person.objects.create(id=6, name="Henry", login="Hehehe", password="12345", usertype=True,
                                        registered=datetime.now())
        docprofile.objects.create(id=2, profile="Отоларинголог")
        Doctor.objects.create(user_id=6, profile_id=2)
        Patient.objects.create(user_id=2)

        person = Person.objects.get(id=sessid)

        # тест
        response = self.client.get(reverse('userpage', kwargs={'id': sessid}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctor.html')

# Тестирование функции авторизации
class ViewFuncTest(TestCase):

    # установка сессии для теста
    def setUp(self):
        # http://code.djangoproject.com/ticket/10899
        settings.SESSION_ENGINE = 'django.contrib.sessions.backends.file'
        engine = import_module(settings.SESSION_ENGINE)
        store = engine.SessionStore()
        store.save()
        self.session = store
        self.client.cookies[settings.SESSION_COOKIE_NAME] = store.session_key

        self.person1 = Person.objects.create(id=1, login="Garfield", password='14231423')
        self.person2 = Person.objects.create(id=2, login="Peter", password='12345')
        self.docprofile1 = docprofile.objects.create(profile="Хирург")
        self.Doctor1 = Doctor.objects.create(id=1, user_id=2, profile_id=1)
        self.Patient1 = Patient.objects.create(user_id=2)
        self.Appoint1 = Appoint.objects.create(id=1, doctor_id=1, patient_id=1, appointdate=datetime(2022, 5, 16), appointtime='11:00')
        self.Appoint2 = Appoint.objects.create(id=2, doctor_id=1, patient_id=1, appointdate=datetime(2022, 5, 14), appointtime='09:00')

    # 8 авторизация
    def testLoginFuncView(self):
        session = self.session
        self.sessid = None
        self.url = reverse('logerror')
        self.user = {"login": 'Garfield', "password": '14231423'}
        response = self.client.post(self.url, self.user)
        auth = False
        person = Person.objects.all()
        for p in person:
            if (self.user['login'] == p.login and self.user['password'] == p.password):

                session['person_id'] = p.id
                session.save()
                self.sessid = session['person_id']
                auth = True

        self.assertEquals(response.status_code, 302)
        self.assertTrue(auth)

    # 9 выход
    def testLogoutFuncView(self):
        session = self.session
        session['person_id'] = 1
        session.save()
        self.url = reverse('logout')
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/')

    # 10 регистрация пациента
    def testRegisterFuncView(self):
        self.url = reverse('createpatient')
        self.registerform = {"login": 'Garfield', "password": '14231423', "name": 'Andrew', "usertype": False}
        response = self.client.post(self.url, self.registerform)
        self.assertEquals(response.status_code, 200)

    # 11 регистрация пользователя администратором
    def testRegisterAdmFuncView(self):
        self.url = reverse('createuser')
        person = Person.objects.get(id=2)
        self.registerform = {"login": 'Garfield', "password": '14231423', "name": 'Andrew', "usertype": False}
        response = self.client.post(self.url, self.registerform)

        self.assertEquals(response.status_code, 200)
        self.assertIsNotNone(person)

    # 12 удаление пользователя администратором
    def testDeleteUserFuncView(self):
        session = self.session
        session['person_id'] = 2
        session.save()

        self.url = reverse('deleteuser', kwargs={"id": 1})
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/adm/')

    # 13 удаление встречи администратором
    def testDeleteAppointmentFuncView(self):
        session = self.session
        session['person_id'] = 1
        session.save()

        self.url = reverse('deleteappointment', kwargs={"id": 1})
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/adm/')








