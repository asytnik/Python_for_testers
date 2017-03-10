# -*- coding: utf-8 -*-
from sys import maxsize

class Param:

    def __init__(self, id=None, lastname=None, firstname=None,  address=None, homephone=None,
                 mobilephone=None, workphone=None, email=None, email2=None, email3=None,
                 all_phones_from_home_page=None, all_email_from_home_page=None, all_db_cont_phones=None,
                 all_db_cont_email=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_email_from_home_page = all_email_from_home_page
        self.id = id
        self.all_db_cont_phones= all_db_cont_phones
        self.all_db_cont_email = all_db_cont_email

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
           and self.lastname == other.lastname and self.firstname == other.firstname \
               and self.address == other.address


    def max_or_id(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize