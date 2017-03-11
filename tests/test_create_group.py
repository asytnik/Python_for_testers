# -*- coding: utf-8 -*-
from model.group import Group


def test_create_group(apl, db, json_groups):
    group = json_groups
    old_groups = db.get_group_info()
    apl.group.creation_group(group)
    new_groups = db.get_group_info()
   # assert len(old_groups) + 1 == len(new_groups) -- can delete, no need yet --
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


