# -*- coding: utf-8 -*-
from model.group import Group


def test_create_group(apl, data_groups):
    group = data_groups
    old_groups = apl.group.get_group_list()
    apl.group.creation_group(group)
    new_groups = apl.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


