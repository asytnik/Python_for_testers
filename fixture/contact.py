# -*- coding: utf-8 -*-

class ContactHelper:

    def __init__(self, Apl):
        self.apl = Apl

    def fill_credentials(self, param):
        wd = self.apl.wd
        self.apl.new_contact_creation()
        self.fill_the_form(param)
        self.enter_credentials()

    def fill_the_form(self, param):
        wd = self.apl.wd
        self.edit_contact_data("firstname", param.firstname)
        self.edit_contact_data("lastname", param.lastname)
        self.edit_contact_data("nickname", param.nickname)
        self.edit_contact_data("title", param.title)
        self.edit_contact_data("company", param.company)
        self.edit_contact_data("address", param.address)

    def edit_contact_data(self, field_name, text):
        wd = self.apl.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def empty_spaces(self, param):
        wd = self.apl.wd
        self.apl.new_contact_creation()
        self.fill_the_form(param)
        self.enter_credentials()

    def enter_credentials(self):
        wd = self.apl.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def del_first_contact(self):
        wd = self.apl.wd
        self.apl.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def counter(self):
        wd = self.apl.wd
        self.apl.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def check_contact_form(self):
        wd = self.apl.wd
        self.choice_modify_contact()
        return len(wd.find_elements_by_name("firstname"))

    def choice_modify_contact(self):
        wd = self.apl.wd
        self.apl.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@title='Details']").click()
        wd.find_element_by_name("modifiy").click()

    def clean_contact_form(self):
        wd = self.apl.wd
        self.choice_modify_contact()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("update").click()
        self.apl.open_home_page()

    def modify_contact_data(self, new_param_data):
        wd = self.apl.wd
        self.choice_modify_contact()
        # fill modify form
        self.fill_the_form(new_param_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.apl.open_home_page()



