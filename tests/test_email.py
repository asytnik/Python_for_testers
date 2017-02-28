# -*- coding: utf-8 -*-

import re

def test_email_on_home_page(apl):
    contact_from_home_page = apl.contact.get_contact_list()[0]
    contact_from_edit_page = apl.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_email_like_home_page(param):
    return "\n".join([param.email, param.email2, param.email3])