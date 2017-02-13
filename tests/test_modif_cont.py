# -*- coding: utf-8 -*-
from model.param import Param

def test_modif_cont(apl):
    if apl.contact.check_contact_form() > 0:
        apl.contact.clean_contact_form()
    apl.contact.modify_contact_data(Param(firstname="Semen"))