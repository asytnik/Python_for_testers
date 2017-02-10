# -*- coding: utf-8 -*-
from model.param import Param

def test_modif_cont(apl):
    apl.contact.modify_contact_data(Param(firstname="Semen", lastname="Gorbunkov", nickname="Professor",
                                          title="Soda", company="A-A-A", address=""))