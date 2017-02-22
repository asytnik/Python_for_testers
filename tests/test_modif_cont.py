# -*- coding: utf-8 -*-
from model.param import Param
from random import randrange

def test_modif_cont(apl):
    if apl.contact.contact_counter() == 0:
        apl.contact.new_contact_creation(Param(firstname="old ivan", lastname="old ivanov"))
    old_contacts = apl.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contacts = Param(firstname="XXXXX", lastname="YYYYYY")
    contacts.id = old_contacts[index].id
    apl.contact.edit_contact_by_index(index, contacts)
    new_contacts = apl.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contacts
    assert sorted(old_contacts, key=Param.max_or_id) == sorted(new_contacts, key=Param.max_or_id)