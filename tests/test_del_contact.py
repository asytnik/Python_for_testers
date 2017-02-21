# -*- coding: utf-8 -*-
from model.param import Param
from random import randrange


def test_del_some_contact(apl):
    if apl.contact.contact_counter() == 0:
        apl.contact.new_contact_creation(Param(firstname="new ivan", lastname="new ivanov"))
    old_contacts = apl.contact.get_contact_list()
    index = randrange(len(old_contacts))
    apl.contact.del_contact_by_index(index)
    new_contacts = apl.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts [index:index+1] = []
    assert old_contacts == new_contacts