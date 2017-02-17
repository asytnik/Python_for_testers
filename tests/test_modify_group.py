# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_fill_group_name(apl):
    if apl.group.counter_group() == 0:
        apl.group.creation_group(Group(name="New group", header="Old header", footer="Old footer"))
    old_groups = apl.group.get_group_list()
    group=Group(name="Old group", header="Old header", footer="Old footer")
    group.id = old_groups[0].id
    apl.group.edit_first_group(group)
    new_groups = apl.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



