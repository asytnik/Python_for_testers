# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Aplicant:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def new_contact_creation(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def destroy(self):
        self.wd.quit()
