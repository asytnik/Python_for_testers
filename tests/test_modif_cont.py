# -*- coding: utf-8 -*-
from model.param import Param
from random import randrange
import random


def test_modif_cont(apl):
    if apl.contact.contact_counter() == 0:
        apl.contact.new_contact_creation(Param(firstname="old ivan", lastname="old ivanov"))
    old_contacts = apl.contact.get_contact_info()
    index = randrange(len(old_contacts))
    contacts = Param(firstname="XXXXX", lastname="YYYYYY")
    contacts.id = old_contacts[index].id
    apl.contact.edit_contact_by_index(index, contacts)
    new_contacts = apl.contact.get_contact_info()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contacts
    assert sorted(old_contacts, key=Param.max_or_id) == sorted(new_contacts, key=Param.max_or_id)


def test_modif_cont_by_id(apl, db, check_ui):
    if len (db.get_contact_info) == 0:
        apl.contact.new_contact_creation(Param(firstname="old ivan", lastname="old ivanov"))
    old_contacts = db.get_contact_info()
    contact = random.choice(old_contacts)
    new_contact_data = Param(firstname="XXXXX", lastname="YYYYYY")
    id = contact.id
    apl.contact.edit_contact_by_id(id, new_contact_data)
    new_contacts = db.get_contact_info()
    assert len(old_contacts) == len(new_contacts)
    mod_contacts = apl.contact.get_contact_info()

    assert sorted(new_contacts, key=Param.max_or_id) == sorted(mod_contacts, key=Param.max_or_id)