# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first_group(apl):
    if apl.group.counter_group() == 0:
        apl.group.creation_group(Group(name="New test"))
    old_groups = apl.group.get_group_list()
    apl.group.delete_first_group()
    new_groups = apl.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
