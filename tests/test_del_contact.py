# -*- coding: utf-8 -*-
from model.param import Param

def test_del_contact(apl):
    if apl.contact.contact_counter() == 0:
        apl.contact.new_contact_creation(Param(firstname="new ivan", lastname="new ivanov", nickname="sorry", title="crecker", company="BBB",
                  address="without"))
    apl.contact.del_first_contact()
