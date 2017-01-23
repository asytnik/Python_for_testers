# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class create_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_create_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login_into(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.creation_group_submit(wd, name="groups", header="jjhjhvbv", footer="gfjgyfghvjgg")
        self.return_to_group_page_logout(wd)

    def test_create_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login_into(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.creation_group_submit(wd, name="", header="", footer="")
        self.return_to_group_page_logout(wd)

    def return_to_group_page_logout(self, wd):
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("Logout").click()

    def creation_group_submit(self, wd, name, header, footer):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill the group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        # submit creation group
        wd.find_element_by_name("submit").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

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