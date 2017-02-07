# -*- coding: utf-8 -*-

class SesOpnContact:

    def __init__(self, Apl):
        self.apl = Apl

    def login_into(self, username, password):
        wd = self.apl.wd
        self.apl.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        # self.apl.new_contact_creation()

    def return_to_HP_logout(self):
        wd = self.apl.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_link_text("Logout").click()
        # self.apl.open_home_page()

    def del_contact(self):
        wd = self.apl.wd
        self.apl.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.apl.open_home_page()








