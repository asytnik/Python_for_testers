# -*- coding: utf-8 -*-
import re
from random import randrange

def test_email_on_home_page(apl):
    home_page_contacts = apl.contact.get_contact_info()
    index = randrange(len(home_page_contacts))
    contact_from_home_page = apl.contact.get_contact_info()[index]
    contact_from_edit_page = apl.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_email_like_home_page(param):
    return "\n".join([param.email, param.email2, param.email3])