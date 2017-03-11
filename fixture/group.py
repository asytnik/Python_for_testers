# -*- coding: utf-8 -*-
from model.group import Group

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
        self.group_cache = None

    def fill_group_form(self, group):
        self.edit_fill_form("group_name", group.name)
        self.edit_fill_form("group_header", group.header)
        self.edit_fill_form("group_footer", group.footer)

    def edit_fill_form(self, field_name, text):
        wd = self.apl.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_first_group(self):
        self.edit_group_by_index(0)

    def edit_group_by_index(self, index, new_group_data):
        wd = self.apl.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill modification
        self.fill_group_form(new_group_data)
        # confirm edition
        wd.find_element_by_name("update").click()
        # return to group page
        self.open_group_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.apl.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.apl.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.apl.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
       # for element in wd.find_elements_by_css_selector("span.group"):
       #     id = element.find_element_by_name("selected[]").get_attribute("value")
       # return id

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.apl.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_group_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.apl.wd
        self.open_group_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_group_page()
        self.group_cache = None

    def open_group_page(self):
        wd = self.apl.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
           wd.find_element_by_link_text("groups").click()

    def counter_group(self):
        wd = self.apl.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_info(self):
        if self.group_cache is None:
            wd = self.apl.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text,id=id))
        return list(self.group_cache)