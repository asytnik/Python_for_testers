# -*- coding: utf-8 -*-

class ContactHelper:

    def __init__(self, Apl):
        self.apl = Apl

    def fill_name_occupation_address(self, param):
        wd = self.apl.wd
        self.apl.new_contact_creation()
        self.fill_the_form(param)
        self.enter_credentials()

    def fill_the_form(self, param):
        wd = self.apl.wd
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

    def empty_name_occupation_address(self, param):
        wd = self.apl.wd
        self.apl.new_contact_creation()
        self.fill_the_form(param)
        self.enter_credentials()

    def modify_name_occupation_address(self, param):
        wd = self.apl.wd
        self.apl.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@title='Details']").click()
        wd.find_element_by_name("modifiy").click()
        self.fill_the_form(param)
        wd.find_element_by_name("update").click()
        self.apl.open_home_page()

    def enter_credentials(self):
        wd = self.apl.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def del_contact(self):
        wd = self.apl.wd
        self.apl.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
