# -*- coding: utf-8 -*-
from model.param import Param

def test_modif_cont(apl):
    if apl.contact.contact_counter() == 0:
        apl.contact.new_contact_creation(Param(firstname="old ivan", lastname="old ivanov", nickname="buddy", title="hooker", company="AAA",
                  address="with address"))
    old_contacts = apl.contact.get_contact_list()
    apl.contact.edit_first_contact(Param(firstname="new ivan", lastname="new ivanov", nickname="sorry", title="crecker", company="BBB",
                  address="without address"))
    new_contacts = apl.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


