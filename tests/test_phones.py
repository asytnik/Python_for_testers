# -*- coding: utf-8 -*-
import re

def test_phones_on_home_page(apl):
    contact_from_home_page = apl.contact.get_contact_list()[0]
    contact_from_edit_page = apl.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_home_page(param):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                   [param.homephone, param.mobilephone, param.workphone]))))