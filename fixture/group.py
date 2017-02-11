# -*- coding: utf-8 -*-

class GroupHelper:

    def __init__(self, Apl):
        self.apl = Apl

    def creation_group(self, group):
        wd = self.apl.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit creation group
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()

    def fill_group_form(self, group):
        wd = self.apl.wd
        self.edit_fill_form("group_name", group.name)
        self.edit_fill_form("group_header", group.header)
        self.edit_fill_form("group_footer", group.footer)

    def edit_fill_form(self, field_name, text):
        wd = self.apl.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_first_group(self, new_group_data):
        wd = self.apl.wd
        self.open_group_page()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill modification
        self.fill_group_form(new_group_data)
        # confirm edition
        wd.find_element_by_name("update").click()
        # return to group page
        self.open_group_page()

    def select_first_group(self):
        wd = self.apl.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_group(self):
        wd = self.apl.wd
        self.open_group_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_group_page()

    def open_group_page(self):
        wd = self.apl.wd
        wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.apl.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def check_empty_form(self):
        wd = self.apl.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        return len(wd.find_elements_by_name("group_name"))