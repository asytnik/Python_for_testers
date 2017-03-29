# -*- coding: utf-8 -*-
from model.param import Param
from random import randrange
import random
import re


def test_modif_cont(apl):
    if apl.contact.contact_counter() == 0:
        apl.contact.new_contact_creation(Param(firstname="old ivan", lastname="old ivanov"))
    old_contacts = apl.contact.get_contact_info()
    index = randrange(len(old_contacts))
    contacts = Param(firstname="XXXXX", lastname="YYYYYY", address="CVCVCVCVCV, NYC, ZIP 10145")
    contacts.id = old_contacts[index].id
    apl.contact.edit_contact_by_index(index, contacts)
    new_contacts = apl.contact.get_contact_info()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contacts
    assert sorted(old_contacts, key=Param.max_or_id) == sorted(new_contacts, key=Param.max_or_id)


def test_modif_cont_by_id(apl, db, check_ui):
    if len(db.get_contact_info()) == 0:
        apl.contact.new_contact_creation(Param(firstname="old ivan", lastname="old ivanov", address="ghgbbb, jhgbvvvv, NYC"))
    old_contacts = db.get_contact_info()
    contact = random.choice(old_contacts)
    modify_data = Param(firstname="RRRRRRR", lastname="WWWWWWW", address="SSSSSSSS")
    id = contact.id
    apl.contact.edit_contact_by_id(id, modify_data)
    new_contacts = db.get_contact_info()
    assert len(old_contacts) == len(new_contacts)
    def clean_string(str):
        return re.sub("\s+", " ", str.strip())
    def clean_param(param):
            return Param(id=param.id, lastname=clean_string(param.lastname), firstname=clean_string(param.firstname), address=clean_string(param.address))
    new_contacts = list(map(clean_param, new_contacts))
    assert sorted(new_contacts, key=Param.max_or_id) == sorted(new_contacts, key=Param.max_or_id)
    if check_ui:
        assert sorted(new_contacts, key=Param.max_or_id) == sorted(apl.contact.get_contact_info(), key=Param.max_or_id)
