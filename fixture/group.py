# -*- coding: utf-8 -*-

class GroupHelper:

    def __init__(self, Apl):
        self.apl = Apl

    def creation_and_submit(self, group):
        wd = self.apl.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill the group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit creation group
        wd.find_element_by_name("submit").click()
        self.apl.open_home_page()


    def open_group_page(self):
        wd = self.apl.wd
        wd.find_element_by_link_text("groups").click()