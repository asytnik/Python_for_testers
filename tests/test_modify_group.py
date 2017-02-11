# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_first_group_name(apl):
    if apl.group.check_empty_form() == 0:
        apl.group.edit_first_group(Group(name="Big boss"))

def test_modify_fill_group_name(apl):
    if apl.group.check_empty_form() > 0:
        apl.group.edit_first_group(Group(name="Old test"))
