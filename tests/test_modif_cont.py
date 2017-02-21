# -*- coding: utf-8 -*-
from model.param import Param

def test_modif_cont(apl):
    if apl.contact.contact_counter() == 0:
        apl.contact.new_contact_creation(Param(firstname="old ivan", lastname="old ivanov"))
    old_contacts = apl.contact.get_contact_list()
    contacts = Param(firstname="mod ivan", lastname="mod ivanov")
    contacts.id = old_contacts[0].id
    apl.contact.edit_first_contact(contacts)
    new_contacts = apl.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contacts
    assert sorted(old_contacts, key=Param.max_or_id) == sorted(new_contacts, key=Param.max_or_id)