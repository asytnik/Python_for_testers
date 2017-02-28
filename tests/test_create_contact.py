# -*- coding: utf-8 -*-

from model.param import Param

def test_create_contact(apl):
    old_contacts = apl.contact.get_contact_list()
    contact = Param(lastname="petrov", firstname="petr", address="1230 Neptune Av.,Queens,NY,11345",
                    homephone="+1 (113) 456", mobilephone="+2225456", workphone="+2 (325) 68-965",
                    email="demo@open-eshop.com", email2="pop2@mail.ru", email3="sanba_sun@credo.com")
    apl.contact.new_contact_creation(contact)
    new_contacts = apl.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Param.max_or_id) == sorted(new_contacts, key=Param.max_or_id)


def test_with_empty_spaces(apl):
    old_contacts = apl.contact.get_contact_list()
    contact = Param(lastname="", firstname="", address="",homephone="", mobilephone="",
                    workphone="", email="", email2="", email3="")
    apl.contact.new_contact_creation(contact)
    new_contacts = apl.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Param.max_or_id) == sorted(new_contacts, key=Param.max_or_id)