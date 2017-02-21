# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_delete_some_group(apl):
    if apl.group.counter_group() == 0:
        apl.group.creation_group(Group(name="New test"))
    old_groups = apl.group.get_group_list()
    index = randrange(len(old_groups))
    apl.group.delete_group_by_index(index)
    new_groups = apl.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups
