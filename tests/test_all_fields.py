# -*- coding: utf-8 -*-
import re
from random import randrange

def test_all_fields_on_home_page(apl):
    home_page_contacts = apl.contact.get_contact_list()
    index = randrange(len(home_page_contacts))
    info_from_home_page = apl.contact.get_contact_list()[index]
    info_from_edit_page = apl.contact.get_contact_info_from_edit_page(index)
    assert info_from_home_page.lastname == info_from_edit_page.lastname
    assert info_from_home_page.firstname == info_from_edit_page.firstname
    assert info_from_home_page.address == info_from_edit_page.address
    assert info_from_home_page.all_email_from_home_page == merge_email_like_home_page(info_from_edit_page)
    assert info_from_home_page.all_phones_from_home_page == merge_phones_like_home_page(info_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_email_like_home_page(param):
    return "\n".join(filter(lambda x: x != "",
                            map(filter(lambda x: x is not None,
                                   [param.email, param.email2, param.email3]))))

def merge_phones_like_home_page(param):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                   [param.homephone, param.mobilephone, param.workphone]))))