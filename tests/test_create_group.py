# -*- coding: utf-8 -*-
from model.group import Group

def test_create_group(apl):
    old_groups = apl.group.get_group_list()
    group=Group(name="kreker", header="pooker", footer="doom")
    apl.group.creation_group(group)
    new_groups = apl.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_create_empty_group(apl):
#   old_groups = apl.group.get_group_list()
#   group=Group(name="", header="", footer="")
#   apl.group.creation_group(group)
#   new_groups = apl.group.get_group_list()
#   assert len(old_groups) + 1 == len(new_groups)
#   old_groups.append(group)
#   assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

