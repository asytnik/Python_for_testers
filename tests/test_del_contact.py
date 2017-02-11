# -*- coding: utf-8 -*-
from model.param import Param

def test_del_contact(apl):
    if apl.contact.counter() == 0:
        apl.contact.fill_credentials(Param(firstname="new ivan", lastname="new ivanov", nickname="sorry", title="crecker", company="BBB",
                  address="without"))
    apl.contact.del_first_contact()
