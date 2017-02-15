# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_fill_group_name(apl):
    if apl.group.counter_group() == 0:
        apl.group.creation_group(Group(name="New group", header="Old header", footer="Old footer"))
    apl.group.edit_first_group(Group(name="Old group", header="Old header", footer="Old footer"))


