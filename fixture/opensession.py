# -*- coding: utf-8 -*-

class OpenSessionHelper:

    def __init__(self, Apl):
        self.apl = Apl

    def enter_credentials(self):
        wd = self.apl.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # self.apl.open_home_page()
        wd.find_element_by_link_text("Logout").click()


    def fill_second_address(self, address2):
        wd = self.apl.wd
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address2)
        self.enter_credentials()

    def fill_e_mail_DOB(self, param):
        wd = self.apl.wd
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(param.email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(param.email2)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[12]").is_selected():
           wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[12]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[11]").is_selected():
           wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[11]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(param.dob)

    def fill_phone_number(self, param):
        wd = self.apl.wd
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(param.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(param.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(param.work)
        wd.find_element_by_name("fax").click()

