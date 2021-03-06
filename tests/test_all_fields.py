# -*- coding: utf-8 -*-
import re
from random import randrange

def test_all_fields_on_home_page(apl):
    home_page_contacts = apl.contact.get_contact_info()
    index = randrange(len(home_page_contacts))
    info_from_home_page = apl.contact.get_contact_info()[index]
    info_from_edit_page = apl.contact.get_contact_info_from_edit_page(index)
    assert clear(info_from_home_page.lastname) == clear(info_from_edit_page.lastname)
    assert clear(info_from_home_page.firstname) == clear(info_from_edit_page.firstname)
    assert clear(info_from_home_page.address) == clear(info_from_edit_page.address)
    assert info_from_home_page.all_email_from_home_page == merge_email_like_home_page(info_from_edit_page)
    assert info_from_home_page.all_phones_from_home_page == merge_phones_like_home_page(info_from_edit_page)
    # с очисткой тест работает на ура
    # Но только с телефонами, а при дополнительной очистке email, через раз.
    # Очистка re.sub "[ ]","",text  как в лекции 5_5 на 16 минуте.

def clear(s):
    return re.sub("[() -]", "", s)

def merge_email_like_home_page(param):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                (filter(lambda x: x is not None,
                                       [param.email, param.email2, param.email3])))))

def merge_phones_like_home_page(param):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [param.homephone, param.mobilephone, param.workphone]))))