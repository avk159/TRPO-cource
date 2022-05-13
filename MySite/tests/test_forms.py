from django.test import SimpleTestCase
from MySite.forms import *

class RegisterTestForms(SimpleTestCase):

    # 1 Register Valid
    def testRegisterFormValid(self):
        form = RegisterForm(data = {
            'login': 'Vasya',
            'name': 'Vasiliy',
            'password': 'lalka',
        })

        self.assertTrue(form.is_valid())

    # 2 Register short login
    def testRegisterFormShortLogin(self):
        form = RegisterForm(data = {
            'login': 'Vas',
            'name': 'Vasiliy',
            'password': 'lalka',
        })

        self.assertFalse(form.is_valid())

    # 3 Register long login
    def testRegisterFormLongLogin(self):
        form = RegisterForm(data = {
            'login': 'VasyaVasyaVasyaVasyaVasya',
            'name': 'Vasiliy',
            'password': 'lal',
        })

        self.assertFalse(form.is_valid())

    # 4 Register short password
    def testRegisterFormShortPassword(self):
        form = RegisterForm(data = {
            'login': 'Vasya',
            'name': 'Vasiliy',
            'password': 'lalk',
        })

        self.assertFalse(form.is_valid())

    # 5 Register long password
    def testRegisterFormLongPassword(self):
        form = RegisterForm(data = {
            'login': 'Vasya',
            'name': 'Vasiliy',
            'password': 'lalkalalkalalkalalkalalka',
        })

        self.assertFalse(form.is_valid())

    # 6 Register short name
    def testRegisterFormShortName(self):
        form = RegisterForm(data = {
            'login': 'Vasya',
            'name': 'Vas',
            'password': 'lalka',
        })

        self.assertFalse(form.is_valid())

    # 7 Register long name
    def testRegisterFormLongName(self):
        form = RegisterForm(data = {
            'login': 'Vasya',
            'name': 'VasiliyVasiliyVasiliy',
            'password': 'lalka',
        })

        self.assertFalse(form.is_valid())

    ########################################

    # 8 Login Valid
    def testLoginFormValid(self):
        form = LoginForm(data={
            'login': 'Vasya',
            'password': 'lalka',
        })

        self.assertTrue(form.is_valid())

    # 9 Login short login
    def testLoginFormShortLogin(self):
        form = LoginForm(data={
            'login': 'Vas',
            'password': 'lalka',
        })

        self.assertFalse(form.is_valid())

    # 10 Login long login
    def testLoginFormLongLogin(self):
        form = LoginForm(data={
            'login': 'VasyaVasyaVasyaVasyaVasya',
            'password': 'lalka',
        })

        self.assertFalse(form.is_valid())

    # 11 Login short password
    def testLoginFormShortPass(self):
        form = LoginForm(data={
            'login': 'Vasya',
            'password': 'lal',
        })

        self.assertFalse(form.is_valid())

    # 12 Login short password
    def testLoginFormLongPass(self):
        form = LoginForm(data={
            'login': 'Vasya',
            'password': 'lalkalalkalalkalalkalalka',
        })

        self.assertFalse(form.is_valid())
