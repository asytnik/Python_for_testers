# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

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
        # open home page
        wd.get("http://localhost/addressbook/")
        # login into
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill name_occupation_address
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("ivan")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("ivanov")
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("balda")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("worker")
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("church")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("1230 Avenue X, Brooklyn, NY")
        # fill phone number
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("+1 113 456 987 654")
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("+2 225 456 874 986")
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("+2 325 685 965 784")
        wd.find_element_by_name("fax").click()
        # fill e-mail_DOB
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("balda@mail.ru")
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("pop2@mail.ru")
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[12]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[11]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[11]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")
        # fill second address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("4554 Neptune Av., Brooklyn,NY")
        # enter_credentials
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # return to hp_logout
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
