# -*- coding: utf-8 -*-

from model.param import Param

class ContactHelper:

    def __init__(self, Apl):
        self.apl = Apl

    def new_contact_creation(self, param):
        wd = self.apl.wd
        wd.find_element_by_link_text("add new").click()
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
        wd.find_element_by_link_text("add new").click()
        self.fill_the_form(param)
        self.enter_credentials()

    def edit_first_contact(self, new_contact_data):
        wd = self.apl.wd
        self.apl.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[7]/a/img").click()
        wd.find_element_by_name("modifiy").click()
        self.fill_the_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.apl.open_home_page()

    def enter_credentials(self):
        wd = self.apl.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def del_first_contact(self):
        wd = self.apl.wd
        self.apl.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def contact_counter(self):
        wd = self.apl.wd
        self.apl.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.apl.wd
        self.apl.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("id")
            firstname=
            lastname=
            contacts.append(Param(firstname=text, lastname=text, id=id))
        return contacts
