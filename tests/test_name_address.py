# -*- coding: utf-8 -*-
import re

def test_name_address_on_home_page(apl):
    name_address_from_home_page = apl.contact.get_contact_list()[0]
    name_address_from_edit_page = apl.contact.get_contact_info_from_edit_page(0)
    assert name_address_from_home_page.lastname == name_address_from_edit_page.lastname
    assert name_address_from_home_page.firstname == name_address_from_edit_page.firstname
    assert name_address_from_home_page.address == name_address_from_edit_page.address


#def clear(s):
#    return re.sub("[() -]", "", s)