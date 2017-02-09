# -*- coding: utf-8 -*-
from model.param import Param

def test_modif_cont(apl):
    apl.contact.modify_name_occupation_address(Param(name="Semen", lastname="Gorbunkov", nickname="Professor",
                                                           title="Soda", company="A-A-A", address=""))