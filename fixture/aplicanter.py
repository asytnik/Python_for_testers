# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.ses_group import SessionHelper
from fixture.group import GroupHelper
from fixture.sescontact import SesOpnContact
from fixture.fillcredentials import FillCredenHelp
from fixture.opensession import OpenSessionHelper


class Aplicant:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.ses_group = SessionHelper(self)
        self.group = GroupHelper(self)
        self.sescontact=SesOpnContact(self)
        self.fillcredentials=FillCredenHelp(self)
        self.opensession=OpenSessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def new_contact_creation(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def destroy(self):
        self.wd.quit()
