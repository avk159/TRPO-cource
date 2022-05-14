from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(ChromeDriverManager().install())

from MySite.models import Person
from selenium.webdriver.common.by import By

class MySeleniumTests(StaticLiveServerTestCase):


    @classmethod
    def setUpClass(cls):
        super(MySeleniumTests, cls).setUpClass()
        cls.selenium = driver
        cls.selenium.implicitly_wait(10)
        person = Person.objects.create(id=1, login='Vova', password='vovan4ik')
        person2 = Person.objects.create(id=2, login='Anna', password='Larionova')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    # 1 Login
    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.selenium.find_element(By.NAME, value="login")
        username_input.send_keys('Vova')
        password_input = self.selenium.find_element(By.NAME, value="password")
        password_input.send_keys('vovan4ik')
        self.selenium.find_element(By.NAME, value='logbutton').click()

    # 2 Register
    def test_register(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/register'))
        username_input = self.selenium.find_element(By.NAME, value="login")
        username_input.send_keys('SeleniumTestUer')
        name_input = self.selenium.find_element(By.NAME, value="name")
        name_input.send_keys('SelTestUs')
        password_input = self.selenium.find_element(By.NAME, value="password")
        password_input.send_keys('qwerty123')
        self.selenium.find_element(By.NAME, value='regbutton').click()

    # 3 About
    def test_about(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.selenium.find_element(By.ID, value='href1').click()

    # 4 Contacts
    def test_contacts(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.selenium.find_element(By.ID, value='href2').click()

    #5 Make Appointment
    def test_makeappointment(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/apptest'))
        select_prof = driver.find_element(By.ID, 'selectBox')
        select_prof = Select(select_prof)
        select_prof.select_by_index(1)
        select_specialist = Select(driver.find_element(By.ID, 'selectBox2'))
        select_specialist.select_by_index(1)
        datepicker = driver.find_element(By.ID, 'date')
        datepicker.click()
        datepicker.send_keys('2205')
        select_time = Select(driver.find_element(By.ID, 'selectbox3'))
        select_time.select_by_index(2)

        driver.find_element(By.ID, 'button').click()

    #6 Delete user on adm page
    def test_deleteuser(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/adm/delete/2'))

    # 7 Delete appointment on adm page
    def test_deleteuser(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/adm/appdelete/2'))












