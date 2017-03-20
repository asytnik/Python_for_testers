# -*- coding: utf-8 -*-
from model.param import Param
import random
import re

def test_del_some_contact(apl, db, check_ui):
    if len(db.get_contact_info()) == 0:
        apl.contact.new_contact_creation(Param(firstname="new ivan", lastname="new ivanov"))
    old_contacts = db.get_contact_info()
    cont = random.choice(old_contacts)
    apl.contact.del_contact_by_id(cont.id)
    new_contacts = db.get_contact_info()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(cont)
    assert old_contacts == new_contacts
    new_contacts = map(clean, db.get_contact_info())
    if check_ui:
        # new_contacts = map(clean, db.get_contact_list()) -- also can insert here --
        assert sorted(new_contacts, key=Param.max_or_id) == sorted(apl.contact.get_contact_info(), key=Param.max_or_id)


def clean(new_contacts):
    return re.sub("[ ]", "", new_contacts)