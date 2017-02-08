# -*- coding: utf-8 -*-

class GroupHelper:

    def __init__(self, Apl):
        self.apl = Apl

    def creation_and_submit(self, group):
        wd = self.apl.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit creation group
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("Logout").click()

    def fill_group_form(self, group):
        wd = self.apl.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def edit_group(self, new_group_data):
        wd = self.apl.wd
        self.open_group_page()
        # select edition group
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # confirm edition
        wd.find_element_by_name("update").click()
        # return to group page
        self.open_group_page()
        wd.find_element_by_link_text("Logout").click()

    def delete_first_group(self):
        wd = self.apl.wd
        self.open_group_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_group_page()
        wd.find_element_by_link_text("Logout").click()

    def open_group_page(self):
        wd = self.apl.wd
        wd.find_element_by_link_text("groups").click()