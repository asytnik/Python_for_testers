# -*- coding: utf-8 -*-
from model.param import Param

def test_del_contact(apl):
    if apl.contact.contact_counter() == 0:
        apl.contact.new_contact_creation(Param(firstname="new ivan", lastname="new ivanov", nickname="sorry", title="crecker", company="BBB",
                  address="without"))
    old_contacts = apl.contact.get_contact_list()
    apl.contact.del_first_contact()
    new_contacts = apl.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts [0:1] = []
    assert old_contacts == new_contacts