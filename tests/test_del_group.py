# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first_group(apl):
    if apl.group.count() == 0:
        apl.group.creation_group(Group(name="New test"))
    apl.group.delete_first_group()
