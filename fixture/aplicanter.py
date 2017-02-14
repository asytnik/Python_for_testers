# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Aplicant:

    def __init__(self):
        self.wd = WebDriver()
        # self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_link_text("home")) > 0):
            return
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
