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
        self.contact_cache = None

    def fill_the_form(self, param):
        wd = self.apl.wd
        self.edit_contact_data("firstname", param.firstname)
        self.edit_contact_data("lastname", param.lastname)
        self.edit_contact_data("address", param.address)
        self.edit_contact_data("home", param.homephone)
        self.edit_contact_data("mobile", param.mobilephone)
        self.edit_contact_data("work", param.workphone)
        self.edit_contact_data("email", param.email)
        self.edit_contact_data("email2", param.email2)
        self.edit_contact_data("email3", param.email3)

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
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.apl.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_the_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.apl.open_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.apl.wd
        self.apl.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")
        cell[7].find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.apl.wd
        self.apl.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")
        cell[6].find_element_by_tag_name("a").click()

    def enter_credentials(self):
        wd = self.apl.wd
        wd.find_element_by_name("submit").click()

    def del_first_contact(self):
        self.del_contact_by_index(0)

    def del_contact_by_index(self, index):
        wd = self.apl.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.apl.wd
        self.apl.open_home_page()
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.apl.wd
        self.apl.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def contact_counter(self):
        wd = self.apl.wd
        self.apl.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.apl.wd
            self.apl.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                id = row.find_element_by_name("selected[]").get_attribute("id")
                cell = row.find_elements_by_tag_name("td")
                lastname = cell[1].text
                firstname = cell[2].text
                address = cell[3].text
                # cell_5 = row.find_elements_by_tag_name("td")
                all_phones = cell[5].text
                all_email = cell[4].text
                self.contact_cache.append(Param(id=id, lastname=lastname, firstname=firstname,
                                                address=address, all_phones_from_home_page=all_phones,
                                                email=all_email[0], email2=all_email[1], email3=all_email[2]))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.apl.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").text
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        return Param(id=id, firstname=firstname, lastname=lastname, address=address,
                     homephone=homephone, mobilephone=mobilephone, workphone=workphone)