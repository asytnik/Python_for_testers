# -*- coding: utf-8 -*-
from model.param import Param

def test_create_contact(apl):
    apl.contact.new_contact_creation(Param(firstname="ivan", lastname="ivanov", nickname="balda", title="worker", company="church",
                                       address="1230 Avenue X, Brooklyn, NY"))

def test_with_empty_spaces(apl):
    apl.contact.empty_spaces(Param(firstname="empty1", lastname="empty2", nickname="", title="", company="", address=""))

