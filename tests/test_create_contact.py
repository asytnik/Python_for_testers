# -*- coding: utf-8 -*-
from model.param import Param

def test_new_contact(apl):
    apl.contact.fill_name_occupation_address(Param(name="ivan", lastname="ivanov", nickname="balda", title="worker", company="church",
                                          address="1230 Avenue X, Brooklyn, NY"))

def test_with_empty_spaces(apl):
    apl.contact.empty_name_occupation_address(Param(name="empty1", lastname="empty2", nickname="", title="", company="",
                                          address=""))

