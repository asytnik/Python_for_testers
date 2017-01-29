# -*- coding: utf-8 -*-

class SessionHelper:

    def __init__(self, App):
        self.app = App

    def login_into(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def return_to_group_page_logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("Logout").click()
