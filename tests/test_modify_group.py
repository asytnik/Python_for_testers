# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_modify_fill_group_name(apl):
    if apl.group.counter_group() == 0:
        apl.group.creation_group(Group(name="New group", header="Old header", footer="Old footer"))
    old_groups = apl.group.get_group_info()
    index = randrange(len(old_groups))
    group=Group(name="Old group", header="Old header", footer="Old footer")
    group.id = old_groups[index].id
    apl.group.edit_group_by_index(index, group)
    new_groups = apl.group.get_group_info()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)