# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from param import Param, Phone, Email

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class new_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_new_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login_into(wd, username="admin", password="secret")
        self.new_contact_creation(wd)
        self.fill_name_occupation_address(wd, Param(name="ivan", lastname="ivanov", nickname="balda", title="worker", company="church",
                                          address="1230 Avenue X, Brooklyn, NY"))
        self.fill_phone_number(wd, Phone(home="+1 113 456 987 654", mobile="+2 225 456 874 986", work="+2 325 685 965 784"))
        self.fill_e_mail_DOB(wd, Email(email1="balda@mail.ru", email2="pop2@mail.ru", dob="1990"))
        self.fill_second_address(wd, address2="4554 Neptune Av., Brooklyn,NY")
        self.enter_credentials(wd)
        self.return_to_HP_logout(wd)

    def test_with_empty_spaces(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login_into(wd, username="admin", password="secret")
        self.new_contact_creation(wd)
        self.fill_name_occupation_address(wd, Param(name="ivan", lastname="ivanov", nickname="balda", title="", company="",
                                          address=""))
        self.fill_phone_number(wd, Phone(home="+1 113 456 987 654", mobile="+2 225 456 874 986", work=""))
        self.fill_e_mail_DOB(wd, Email(email1="balda@mail.ru", email2="", dob="1990"))
        self.fill_second_address(wd, address2="")
        self.enter_credentials(wd)
        self.return_to_HP_logout(wd)

    def return_to_HP_logout(self, wd):
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_link_text("Logout").click()

    def enter_credentials(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_second_address(self, wd, address2):
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address2)

    def fill_e_mail_DOB(self, wd, param):
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(param.email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(param.email2)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[12]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[11]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[11]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(param.dob)

    def fill_phone_number(self, wd, param):
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(param.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(param.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(param.work)
        wd.find_element_by_name("fax").click()

    def fill_name_occupation_address(self, wd, param):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(param.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(param.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(param.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(param.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(param.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(param.address)

    def new_contact_creation(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login_into(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
