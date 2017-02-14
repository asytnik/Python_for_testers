# -*- coding: utf-8 -*-
from model.param import Param

def test_modif_cont(apl):
    if apl.contact.contact_counter() > 0:
        apl.contact.del_first_contact()
    apl.contact.fill_credentials(Param(firstname="new ivan", lastname="new ivanov", nickname="sorry", title="crecker", company="BBB",
                  address="without"))

