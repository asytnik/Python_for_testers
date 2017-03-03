# -*- coding: utf-8 -*-
import pytest
from model.param import Param
from data.contacts import constant as testdata

@pytest.mark.parametrize("param", testdata, ids=[repr(x) for x in testdata])
def test_create_contact(apl,param):
    old_contacts = apl.contact.get_contact_list()
    apl.contact.new_contact_creation(param)
    new_contacts = apl.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(param)
    assert sorted(old_contacts, key=Param.max_or_id) == sorted(new_contacts, key=Param.max_or_id)


#def test_with_empty_spaces(apl):
#    old_contacts = apl.contact.get_contact_list()
#    contact = Param(lastname="", firstname="", address="",homephone="", mobilephone="",
#                    workphone="", email="", email2="", email3="")
#    apl.contact.new_contact_creation(contact)
#    new_contacts = apl.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Param.max_or_id) == sorted(new_contacts, key=Param.max_or_id)